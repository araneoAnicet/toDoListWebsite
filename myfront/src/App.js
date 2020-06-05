/* eslint-disable react/jsx-no-comment-textnodes */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react';
import './Components/App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import "bootswatch/dist/lux/bootstrap.min.css"
import Header from './Components/Header.js'
import LoginForm from './Components/LoginForm';

function App() {
  return (
    <div>
      <Header />
      <LoginForm />

{/*
      <form>
  <fieldset>
    <legend>Legend</legend>
    <div class="form-group row">
      <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
      <div class="col-sm-10">
        <input type="text" readonly="" class="form-control-plaintext" id="staticEmail" value="email@example.com"></input>
      </div>
    </div>
    <div class="form-group">
      <label for="exampleInputEmail1">Email address</label>
      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email"></input>
      <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
    </div>
    <div class="form-group">
      <label for="exampleInputPassword1">Password</label>
      <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password"></input>
    </div>
    
    <button type="submit" class="btn btn-primary">Submit</button>
  </fieldset>
</form>
*/}
</div>

  )
}

export default App;
