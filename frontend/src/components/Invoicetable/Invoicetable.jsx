import "./invoicetable.scss";
import { DataGrid } from '@mui/x-data-grid';
import { randomCreatedDate, randomUpdatedDate } from '@mui/x-data-grid-generator';
import { Link } from "react-router-dom";
import { FiPlus } from "react-icons/fi";

const columns = [
    { field: 'id', headerName: 'ID', flex:0.5  },
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
        field: "status",
        headerName: "Status",
        flex:1,
        renderCell: (params) => {
          return (
            <div className={`cellWithStatus ${params.row.status}`}>
              {params.row.status}
            </div>
          );
        },
      },
  ];

  const rows = [
    { 
        id: 1, 
        customer: 'Snow', 
        amount: 35, 
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "paid" 
    },
    { 
        id: 2, 
        customer: 'Lannister', 
        amount: 42,
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "paid" 
    },
    { 
        id: 3, 
        customer: 'Lannister', 
        amount: 45,
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "pending"  
    },
    { 
        id: 4, 
        customer: 'Stark', 
        amount: 16,
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "draft"  
    },
    { id: 5, 
        customer: 'Targaryen', 
        amount: 10,
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "paid"  
    },
    { 
        id: 6, 
        customer: 'Melisandre', 
        amount: 150,
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "pending" 
    },
    { 
        id: 7, 
        customer: 'Clifford', 
        amount: 44,
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "pending" 
    },
    { 
        id: 8,
        customer: 'Frances', 
        amount: 36,
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "paid" 
    },
    { 
        id: 9, 
        customer: 'Roxie',
        amount: 65,
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "draft"
    },
    { 
        id: 10, 
        customer: 'Roxie',
        amount: 65,
        invoice_date:  randomCreatedDate(), 
        payment_method: 'cash',
        payment_to_date:  randomUpdatedDate(),
        status: "pending"
    },
  ];
    
  

const Invoicetable = () => {
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

export default Invoicetable