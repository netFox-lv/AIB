import './App.css';
import React from 'react'

const BasicForm = () => {
  return (
    <>
    <form method="POST" name="login" id="quick_login_form">
    <div>
      <header>Welcome to AIB</header>
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
    <input type="text" name="password" id="password"/>
    </div>

    <div>
      <button>GO</button>
    </div>
    </form>
    </>
  )
}

export default BasicForm;