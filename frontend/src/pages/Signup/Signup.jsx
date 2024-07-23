import './Signup.css'
import Header  from '../../components/Header/Header'
import { NavLink } from 'react-router-dom'
export const SignUp = ()=>{
    return (
       
    <div className='MainContainer'>
               
        <div className="container">
     
            <div className="form-container">
                <h2 className='heading'>Register</h2>
                <form>
                    <div className="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" name="email" required></input>
                    </div>
                    <div className="form-group">
                        <label for="phone">Phone Number</label>
                        <input type="tel" id="password" name="phone" required></input>
                    </div>
                    <div className="form-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" name="password" required></input>
                    </div>
                    <div className="form-group">
                        <label for="confirm-password">Confirm Password</label>
                        <input type="password" id="confirm-password" name="confirm-password" required></input>
                    </div>
                    <button type="submit">Register</button>
                    <div className='login-link'>
                        <NavLink  to={'/auth/login'}>Already have an account? Login</NavLink>
                    </div>
                    
                </form>
              </div>
           </div>
         </div>
    )
}

