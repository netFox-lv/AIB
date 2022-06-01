import "./home.scss";
import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import Widget from "../../components/widget/Widget";
import Chart from "../../components/chart/Chart";
import Progressbar from "../../components/progressbar/Progressbar";
import Table from "../../components/table/Table";
import axios from "axios";

const is_logged_url = 'http://127.0.0.1:8000/api/loginInfo';
const login_url = "http://127.0.0.1:3000/";

const Home = () => {

  axios.get(is_logged_url)
  .then(res => {
    if (!res.data['logged_in']){
      window.location.replace(login_url);
    }
  });

  return (
    <div className='home'>
        <Sidebar />
        <div className="homeContainer">
          <Navbar />
          <div className="widgets">
            <Widget type="unresolved"/>
            <Widget type="new agreements"/>
            <Widget type="finished"/>
            <Widget type="drafts"/>
          </div>
          <div className="charts">
            <Chart/>
            <Progressbar/>
          </div>
          <div className="listContainer">
            <h3 className="listName">Recent Invoices</h3>
            <Table/>
          </div>
        </div>
    </div>
  )
}

export default Home
