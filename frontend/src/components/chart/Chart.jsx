import "./chart.scss"
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { useEffect, useState } from "react";
import axios from "axios";

const get_monthly_income_url = 'http://127.0.0.1:8000/api/incPerMonth';

  export default function Chart(){
  const [data, setData] = useState({data:[]});

  useEffect(() => {
    async function fetchData(){
      const mas = await axios
      .get(get_monthly_income_url)
      .then(function (res) {
        console.log(res.status);
        if(res.status !== 404){
          let table = res.data['data'];
          let result = [];
          let months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
          table.forEach(element => {
            result.push({
              name: months[element[0]-1],
              Total: (element[1] === null)?0:(element[1])
            });
          });
          return result;
        }
      })
      .catch(function (e){
        console.log(e);
      });
      setData({data: mas});
    }
    fetchData();
  }, []);

  return (
    <div className="chart">
        <h3 className="title">Income Analytics</h3>
        <ResponsiveContainer width="100%" height="80%">
        <AreaChart width={730} height={250} data={data.data}
  margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
  <defs>
    <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
      <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8}/>
      <stop offset="95%" stopColor="#8884d8" stopOpacity={0}/>
    </linearGradient>
    
  </defs>
  <XAxis dataKey="name" />
  <YAxis />
  <CartesianGrid strokeDasharray="3 3" />
  <Tooltip />
  <Area type="monotone" dataKey="Total" stroke="#8884d8" fillOpacity={1} fill="url(#colorUv)" />
  
</AreaChart>
      </ResponsiveContainer>
    </div>
  )
}