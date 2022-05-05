import "./table.scss";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { useEffect, useState } from "react";
import axios from "axios";

const get_recents_url = 'http://127.0.0.1:8000/api/recentInv';

export default function List() {
  
  const [data, setData] = useState({ invoices: [] });

  useEffect(() => {
    async function fetchData() {
      const data = await axios
        .get(get_recents_url)
        .then(function (res) {
          console.log(res.status);
          if (res.status !== 404) {
            let table = res.data["data"];
            let invoices = [];
            table.forEach(element => {
              invoices.push({
                id: element["id"],
                customer: element["customer"],
                date: element["invoice_date"],
                amount: element["amount"],
                method: element["payment_method"],
                status: ((element["paid"]) ? "Approved" : "Pending"),
              });
            });
            return invoices;
          }
        }).catch(function (e) {
          console.log(e);
        });
      setData({ invoices: data });
    }

    fetchData();
  },[]);

  return (
    <TableContainer component={Paper} className="table">
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell className="tableCell">ID</TableCell>
            <TableCell className="tableCell">Customer</TableCell>
            <TableCell className="tableCell">Date</TableCell>
            <TableCell className="tableCell">Amount</TableCell>
            <TableCell className="tableCell">Payment Method</TableCell>
            <TableCell className="tableCell">Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.invoices.map((row) => (
            <TableRow key={row.id}>
              <TableCell className="tableCell">{row.id}</TableCell>
              <TableCell className="tableCell">{row.customer}</TableCell>
              <TableCell className="tableCell">{row.date}</TableCell>
              <TableCell className="tableCell">{row.amount}</TableCell>
              <TableCell className="tableCell">{row.method}</TableCell>
              <TableCell className="tableCell">
                <span className={`status ${row.status}`}>{row.status}</span>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );

};