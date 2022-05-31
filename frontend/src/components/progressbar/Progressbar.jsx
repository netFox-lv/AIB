import "./progressbar.scss"
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import { CircularProgressbarWithChildren } from 'react-circular-progressbar';
import { useEffect, useState } from "react";
import axios from "axios";

let percentage = 0;
const stats_url = "http://127.0.0.1:8000/api/progress";

export default function Progressbar() {

  const [data, setData] = useState({ earned: 0, total: 0 });
  useEffect(() => {
    async function fetchData() {
      const result = await axios.get(stats_url)
        .then(function (res) {
          let earned = (res.data["earned"] == null) ? 0 : res.data["earned"];
          let total = (res.data["total"] == null) ? 0 : res.data["total"];
          return { earned: earned, total: total };
        })
        .catch((e) => console.log(e));
      setData({ earned: result.earned, total: result.total });
    }
    fetchData();
  }, []);

  percentage = (data.earned / data.total) * 100;
  return (
    <div className="progressbar">
      <div className="top">
        <h3 className="title">Statistics</h3>
        <div className="subtitle">This year</div>
      </div>
      <div className="featchart">
        <CircularProgressbar value={percentage} text={`$23,600`}
          styles={buildStyles({
            // Whether to use rounded or flat corners on the ends - can use 'butt' or 'round'
            strokeLinecap: 'butt',

            // Text size
            textSize: '16px',

            // Colors
            pathColor: `#3751FF`,
            textColor: '#252733',
            trailColor: '#F0F2FF',
            backgroundColor: '#3751FF',
          })}
        />
      </div>
      <div className="bottom">
        <div className="section">
          <p className="amount">${data.total - data.earned}</p>
          <p className="name">Left</p>
        </div>
        <div className="section">
          <p className="amount">${data.total}</p>
          <p className="name">Required</p>
        </div>
      </div>
    </div>
  )
}