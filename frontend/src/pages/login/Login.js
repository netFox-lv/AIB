import './login.css';
import React from 'react'
import axios from "axios";

const is_logged_url = 'http://127.0.0.1:8000/api/loginInfo';
const home_url = "http://127.0.0.1:3000/home";

let handleDubmit = async (e) => {
  e.preventDefault();
  axios.post('http://127.0.0.1:8000/api/login',{
    withCredentials: true,
    email: document.getElementById("email").value,
    password: document.getElementById("password").value
  })
  .then(res => {
    if (res.data['access_granted']===true){
      window.location.replace(home_url);
    } else { 
      document.getElementById("error_label").style ="color: red;text-align: center; font-size: 16px;";
      document.getElementById("error_label").innerHTML= "Invalid email or password. <BR> Please try again";
      document.getElementById("password").value='';
    }
  })
  .catch((e) => {
    console.log(e);
  });
}



const BasicForm = () => {

  axios.get(is_logged_url)
  .then(res => {
    if (res.data['logged_in']){
      window.location.replace(home_url);
    }
  });
 
  return (
    
  <div class="square-container">
        <ul class="square">
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
        </ul>

    <form id="quick_login_form" onSubmit ={handleDubmit}>
    <link href='https://fonts.googleapis.com/css?family=Poppins' rel='stylesheet'/>
      <div class="login_form">
        <div id= "logo">
           <span class="center"> 
            <img src={require ('../../img/logo/logo.png')} alt="Logo" width="80px" class="image"/>
           </span>
        </div>
        <div class ="login_form_text">
          <p id ="first_line">Log in to AIB</p>
          <p id = "second_line">Enter your email and password bellow</p>
        </div>
        <p id="error_label"></p> 
        <div class = "login_input_forms">
          <div class = "email_input">
            <label htmlFor="email" id="email_label">EMAIL</label><br/>
            <input type="email" placeholder='Email address'  id="email"/><br/>
          </div>
          <div class = "password_input">
            <label htmlFor="password" id="pass_label">PASSWORD</label><br/>
            <input type="password" placeholder='Password' id="password"/><br/>
          </div>
        </div>
        <div class = "login_bttn_forms">
          <button className='login_bttn' type="submit">Log In</button>
        </div>
      </div>
    </form>
  </div>
  
  )

}
export default BasicForm;