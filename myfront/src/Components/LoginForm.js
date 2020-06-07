import React,{ Component } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import "bootswatch/dist/lux/bootstrap.min.css";


class LoginForm extends Component {
    render(){
    return(
        
        <div>
            <form className="LoginForm-margin">
                <fieldset>
                    <legend>Log in</legend>
                    
                        <div className="form-group">
                            <label for="exampleInputEmail1">Email address</label>
                            <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email"></input>
                            <small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
                        </div>

                        <div className="form-group">
                            <label for="exampleInputPassword1">Password</label>
                            <input type="password" className="form-control" id="exampleInputPassword1" placeholder="Password"></input>
                        </div>

                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="exampleCheck1"></input>
                            <label class="form-check-label" for="exampleCheck1">Check me out</label>
                        </div>
                    
                        <button type="button" className="btn btn-primary">Sign in</button>
                        <button type="button" className="btn btn-secondary">Sign up</button>
                </fieldset>
            </form>
        </div>
        
)
    }
}

export default LoginForm;