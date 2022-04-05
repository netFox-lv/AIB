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
          <h3>A</h3>
          
          <div>
            <h1>Log in to AIB</h1>
          </div>
          <br/>
          <div>
            <label htmlFor="email" id="email_label">Email</label></div>
          <div>
              <input type="text" name="email" id="email"/>
          </div>
          <div>
            <label htmlFor="password" id="pass_label">Password</label>
          </div>
          <div>
            <input type="text" name="password" id="password"/>
          </div>
            <div>
              <h2>
                <button id="login_bttn">Log in</button>
              </h2>
            </div>
          </form>
  
           

  </div>
  )
}
export default BasicForm;