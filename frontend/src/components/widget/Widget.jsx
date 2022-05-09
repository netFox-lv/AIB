import axios from "axios";
import { useEffect, useState } from "react";
import "./widget.scss"

const unresolved_url = 'http://127.0.0.1:8000/api/unresolvedInv';
const new_url = 'http://127.0.0.1:8000/api/newAgr';
const finished_url = 'http://127.0.0.1:8000/api/finishedAgr';
const drafts_url = 'http://127.0.0.1:8000/api/draftcount';

export default function Widget({ type }) {
  const [data, setData] = useState({ title: "", count: 0 });

  useEffect(() => {
    async function fetchData() {
      let ask;
      let title;
      switch (type) {
        case "unresolved":
          ask = unresolved_url;
          title = "Unresolved";
          break;
        case "new agreements":
          ask = new_url;
          title = "New agreements";
          break;
        case "finished":
          ask = finished_url;
          title = "Finished";
          break;
        case "drafts":
          ask = drafts_url;
          title = "Drafts";
          break;
        default:
          break;
      }
      const count = await axios
        .get(ask)
        .then(function (res) {
          console.log(res.status)
          if (res.status !== 404) {
            return res.data['count'];
          }
        }).catch(function (e) {
          console.log(e);
          return 0;
        });
      setData({title: title, count: count});
    }
    fetchData();
  }, [])

  return (
    <div className="widget">
      <div className="content">
        <span className="title">{data.title}</span>
        <span className="count">{data.count}</span>
      </div>

    </div>
  )
}

