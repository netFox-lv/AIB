import "./agreements.scss";
import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import Table from "../../components/table/Table";

const Agreement = () => {
  return (
    <div className='agreement'>
        <Sidebar />
        <div className="agreementContainer">
          <Navbar />
          <div className="listContainer">
            <h3 className="listName">All agreements</h3>
            <Table/>
          </div>
        </div>
    </div>
  )
}

export default Agreement