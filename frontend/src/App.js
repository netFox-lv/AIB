import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import Invoice from "./pages/invoices/Invoice";
import New from "./pages/new/New";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import axios from "axios";

function App() {
  axios.defaults.withCredentials = true;
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/">
            <Route index element={<Login />} />
            <Route path="home" element={<Home />} />
            <Route path="invoice">
              <Route index element={<Invoice />}/>
              <Route path="new" element={<New />} />
            </Route>
            </Route>
          </Routes>  
      </BrowserRouter>
    </div>
  );
}

export default App;
