import "./invoicetable.scss";
import { DataGrid } from '@mui/x-data-grid';
import { randomCreatedDate, randomUpdatedDate } from '@mui/x-data-grid-generator';
import { Link } from "react-router-dom";
import { FiPlus } from "react-icons/fi";
import { useEffect, useState } from "react";
import axios from "axios";

const all_invoices_url = "http://127.0.0.1:8000/api/invoice/all"

const columns = [
    { field: 'invoice_number', headerName: 'Invoice number', flex:1  },
    { field: 'customer', headerName: 'Customer', flex:1 },
    {
      field: 'amount',
      headerName: 'Amount',
      flex:1
    },
    {
        field: 'invoice_date',
        headerName: 'Invoice date',
        type: 'date',
        flex:1
      },
    {
        field: 'payment_method',
        headerName: 'Invoice type',
        flex:1
      },
    {
      field: 'payment_to_date',
      headerName: 'Payment date',
      type: 'date',
      flex:1
    },
    {
        field: "paid",
        headerName: "Status",
        flex:1,
        renderCell: (params) => {
          return (
            <div className={`cellWithStatus ${params.row.paid}`}>
              {params.row.paid}
            </div>
          );
        },
      },
  ];
    
  

export default function Invoicetable(){

  const [rows, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const result = await axios.get(all_invoices_url)
        .then(function (res) {
          let rows = res.data.data;
          for (let i = 0; i<rows.length; i++){
            rows[i]["paid"]=((rows[i]["paid"]==true)?"paid":"pending"); //convert from boolean to paid or pending
          }
          console.log(rows);
          return rows;
        })
        .catch((e) => console.log(e));
      setData(result);
    }
    fetchData();
  }, []);

  return (
    
    <div className="invoicetable">
        <div className="datatableTitle">
        All Invoices
        <Link to="/invoice/new" className="link">
            <div className="content">
            <FiPlus className="icon" />
            New Invoice
            </div>
        </Link>
      </div>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={9}
        rowsPerPageOptions={[9]}
      />
      
    </div>
  )
}