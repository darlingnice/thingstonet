import './Header.css'
import { NavLink } from 'react-router-dom';
const Header = ()=>{

    return (

        <div className="Header">
            <div className='logo-container'>
             
                <label className="logo">Intanet</label>
            </div>
            <div className='nav-container'>
                <ul className='nav'> 
                    <li><NavLink to={"/"}>Home</NavLink></li>
                    <li><NavLink to={"/auth/about"}>About</NavLink></li>
                    <li><NavLink to={"/auth/services"}>Services</NavLink></li>
                    <li><NavLink to={"/auth/signup"}>Register</NavLink></li>
                    <li><NavLink  to={"/auth/login"}>Login</NavLink></li> 
                </ul> 
            </div>
            

        </div>
    );
}


export default Header;