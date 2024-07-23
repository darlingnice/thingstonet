import { NavLink } from 'react-router-dom';
import './Footer.css'

const Footer =()=>{
    return (
        <>
        <div className="Footer">
        <div className="footer-container">
            <div className="footer-section">
                <h2>About Us</h2>
                <p>We are a team of passionate developers dedicated to creating the best user experiences.</p>
            </div>
            <div className="footer-section">
                <h2>Quick Links</h2>
                <NavLink to={"#"}>Home</NavLink>
                <NavLink to={"#"}>Services</NavLink>
                <NavLink to={"#"}>Contact</NavLink>
                <NavLink to={"#"}>Blog</NavLink>
                <NavLink to={"#"}>Home</NavLink>
            </div>
            <div className="footer-section">
                <h2>Follow Us</h2>
                <div className="social-icons">
                  
                </div>
            </div>
        </div>
        <div className="footer-bottom">
            <p>&copy; 2024 Intanet. All rights reserved.</p>
        </div>
   
        </div>
        </>

    );
}

export default Footer;