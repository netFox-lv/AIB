import './App.css';
import React from 'react'

const BasicForm = () => {
  return (
    <>
    <form method="POST" name="login" id="quick_login_form">
    <h3>A</h3><div>
      <h1>Log in to AIB</h1>
    </div>
    <h1></h1>

  <div>
   <label htmlFor="email">Email</label></div>

  <div>
      <input type="text" name="email" id="email"/>
    </div>
  
  <div>
    <label htmlFor="password">Password</label></div>

  <div>
    <input type="text" name="password" id="password"/></div>

    <h1></h1>

    <div>
      <h2>
      <button>Log in</button>
    </h2></div>
    </form>
    </>
  )
}

export default BasicForm;