import "./new.scss"
import Navbar from '../../components/navbar/Navbar'
import Sidebar from '../../components/sidebar/Sidebar'
import { Link } from "react-router-dom";

const New = () => {
  return (
    <div className="new">
        <Sidebar />
        <div className="container">
            <Navbar />
            <div className="cont">
              <div className="name">
                Add new invoice
              </div>
              <form>
                <div className="elements">
                  <div className="formInput">
                    <label>Customer</label>
                    <input type="text"/>
                  </div>
                  <div className="formInput">
                    <label>Amount</label>
                    <input type="text"/>
                  </div>
                  <div className="formInput">
                    <label>Invoice date</label>
                    <input type="date"/>
                  </div>
                  <div className="formInput">
                    <label>Invoice type</label>
                    <input type="text"/>
                  </div>
                  <div className="formInput">
                    <label>Payment date</label>
                    <input type="date"/>
                  </div>
                  <div className="formInput">
                    <label>Status</label>
                    <input type="radio"/>
                  </div>
                </div>
                  <Link to="/invoice" className="link">
                    <button className="cancel">Cancel</button>
                    <button className="save">Save Invoice</button>
                  </Link>
              </form>
            </div>
        </div>
      </div>
  )
}

export default New