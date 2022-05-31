import "./navbar.scss"
import { FiBell } from "react-icons/fi";
import { useEffect, useState } from "react";
import axios from "axios";

const get_username_url = 'http://127.0.0.1:8000/api/loginInfo';

export default function Navbar() {

  const [data, setData] = useState({ username: "Test User Name" });
  useEffect(() => {
    async function fetchData() {
      const name = await axios.get(get_username_url)
        .then(function (res) {
          return res.data["username"];
        })
        .catch(function (e) {
          console.log();
        });
      setData({ username: name });
    }
    fetchData();
  }, []);

  return (
    <div className='navbar'>
      <div className='wrapper'>
        <div className='items'>
          <div className="item">
            <FiBell className="icon" />
          </div>
          <div className="item">
            {data.username}
          </div>
          <div className="item">
            <img
              src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
              alt="avatar"
              className="avatar" />

          </div>
        </div>
      </div>
    </div>
  )
}
