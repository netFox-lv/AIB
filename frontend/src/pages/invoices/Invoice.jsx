import "./invoice.scss"
import Sidebar from "../../components/sidebar/Sidebar"
import Navbar from "../../components/navbar/Navbar"
import Invoicetable from "../../components/Invoicetable/Invoicetable"

const Invoice = () => {
  return (
    
    <div className="invoice">
      <Sidebar/>
      <div className="invoiceContainer">
        <Navbar/>
        <div className="table">
          
          <Invoicetable/>
        </div>
      </div>
    </div>
  )
}

export default Invoice