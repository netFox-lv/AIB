import "./chart.scss"
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
    { name: "Jan", Total: 1200 },
    { name: "Feb", Total: 2100 },
    { name: "Mar", Total: 800 },
    { name: "Apr", Total: 1600 },
    { name: "May", Total: 900 },
    { name: "Jun", Total: 1700 },
    { name: "Jul", Total: 1200 },
    { name: "Aug", Total: 2100 },
    { name: "Sep", Total: 1600 },
    { name: "Oct", Total: 1900 },
    { name: "Nov", Total: 900 },
    { name: "Dec", Total: 700 },
  ];

const Chart = () => {
  return (
    <div className="chart">
        <h3 className="title">Income Analytics</h3>
        <ResponsiveContainer width="100%" height="80%">
        <AreaChart width={730} height={250} data={data}
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

export default Chart