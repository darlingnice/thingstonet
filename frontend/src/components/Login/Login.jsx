
import './Login.css'
import { NavLink } from "react-router-dom"
const Login = ()=>{
    return (
        <div className="Login">
                <div className='login-container'>
                    <h2 className='heading'>Login</h2>
                    <form action="/login" method="post">
                        <input type="text" name="username" placeholder="Username" required></input>
                        <input type="password" name="password" placeholder="Password" required></input>
                        <NavLink  id={'link'} to={"/auth/forgot-pass"}>Forgot Password</NavLink>
                        <button id='btn-login' type="submit">Login</button>
                    </form>
                    <div className='register-link'>
                    <NavLink  to={'/auth/signup'}>Don't have an account? Register</NavLink>
                    </div>

            </div>
            
      </div>
    )
}
export default Login;