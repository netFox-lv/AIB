import './App.css';
import React from 'react'
import '../src/App.css';



let handleDubmit = async (e) => {
  e.preventDefault();
  try {
    const url=`http://127.0.0.1:8000/api/login/${document.getElementById("email").value}/${document.getElementById("password").value}`;
    let res = await fetch(url, {
      method:"GET"
    });
    let resJSON = await res.json();
    if (resJSON['access_granted']===true){
      window.location.replace("http://127.0.0.1:8000/admin/");
    } else { 
      window.location.replace("http://127.0.0.1:3000/");
    }
  } catch (err) {
    console.log(err);
  }
}


const BasicForm = () => {

 
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
            <img src={require('../src/img/logo/logo.png')} alt="Logo" width="80px" class="image"/>
           </span>
        </div>
        <div class ="login_form_text">
           <p id ="first_line">Log in to AIB</p>
          <p id = "second_line">Enter your email and password bellow</p>
        </div>
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

