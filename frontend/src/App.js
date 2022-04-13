import './App.css';
import React from 'react'

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

    <form method="POST" name="login" id="quick_login_form">
      <div class="login_form">
        <div id= "logo">
            <img src="https://i.pinimg.com/736x/b5/b8/be/b5b8bee6288e54a777307fa000786620.jpg" 
            width="200px" height="200px" id='png'></img>
        </div>
        <div class ="login_form_text">
          <h1>Log in to AIB</h1>
          <h2>Enter your email and password bellow</h2>
        </div>
        <div class = "login_input_forms">
          <p>
            <label htmlFor="email" id="email_label">EMAIL</label>
            <input type="text" placeholder='Email address' name="email" id="email"/>
          </p>
          <p>
            <label htmlFor="password" id="pass_label">PASSWORD</label>
            <input type="text" placeholder='Password' name="password" id="password"/>
          </p>
        </div>
        <div class = "login_bttn_forms">
          <p><button id ="login_bttn">Log in</button></p>
        </div>
      </div>
    </form>
  </div>
  )
}
export default BasicForm;