import "./sidebar.scss"
import { FiPieChart, FiEdit, FiInbox, FiTrendingUp, FiLogOut } from "react-icons/fi";
import { Link } from "react-router-dom";
import axios from "axios";
function logout(){
  axios.get("http://127.0.0.1:8000/api/logout")
}
const Sidebar = () => {
  return (
    <div className='sidebar'>
        <div className="top">
          <Link to="/" style={{ textDecoration: "none" }}>
            <span className="logo">AIB</span>
          </Link>
        </div>
        <div className="menu">
          <ul>
            <li>
              <FiPieChart className="icon" />
              <span>Dashboard</span>
            </li>
            <li>
              <FiEdit className="icon" />
              <span>Agreements</span>
            </li>
            <li>
              <FiInbox className="icon" />
              <span>Invoices</span>
            </li>
            <li>
              <FiTrendingUp className="icon" />
              <span>Budget</span>
            </li>
          </ul>
          <hr />
          <ul>
          <Link to="/" style={{ textDecoration: "none" }}  onclick="logout()">
            <li>
              <FiLogOut className="icon" />
              <span>Log Out</span>
            </li>
          </Link>
          </ul>
        </div>
    </div>
  )
}

export default Sidebar