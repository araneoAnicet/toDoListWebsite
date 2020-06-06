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
    </div>

  )
}

export default App;
