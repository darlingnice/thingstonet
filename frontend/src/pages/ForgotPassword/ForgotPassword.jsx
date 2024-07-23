import { NavLink } from 'react-router-dom'
import './ForgotPassword.css'
import { Logo } from '../../components/Logo/Logo'
export const ForgotPassword = ()=>{
    return (
        <>
            <Logo/>
            <div className="ForgotPassword">
                
                <div className="forgot-password-form">
                    <h1>Forgot Password</h1>
                    <p>Enter your email address below and we'll send you a link to reset your password.</p>
                    <form action="/send-reset-link" method="POST">
                        <label for="email">Email Address</label>
                        <input type="email" id="email" name="email" required></input>
                        <button id='btn-send-reset-link' type="submit">Send Reset Link</button>
                        <div id='back-to-login-link'>
                        <NavLink  to={'/auth/login'}> Back to Login</NavLink>
                        </div>
                       
                    </form>
                </div>
            </div>
        
        </>
    )
}