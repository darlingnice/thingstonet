import Header from "../../components/Header/Header";
import Sidenav from "../../components/Sidenav/Sidenav";
import Maincontent from "../../components/Maincontent/Maincontent";
import Footer from "../../components/Footer/Footer";
import './About.css'
const About = ()=>{
    return (
        <div  className="About" >
                <Header/>
        
            <div className="container">
                <div>
                <h2>About Intanet</h2>
                <p>Welcome to Intanet, your trusted Internet of Things (IoT) solutions provider.
                     At Intanet, we are dedicated to delivering innovative and reliable IoT solutions 
                     that empower businesses and individuals to connect, monitor, and control their environments 
                     seamlessly.</p>
                <h3>Our Mission</h3>
                <p>Our mission is to provide cutting-edge IoT technologies that enhance efficiency, improve
                     safety, and drive sustainable growth. We strive to make the world smarter, safer, and more
                      connected through our comprehensive range of IoT services and products.</p>
                <h3>What We Offer</h3>
                <ul>
                    <li>Custom IoT Solutions</li>
                    <li>Smart Home Automation</li>
                    <li>Industrial IoT Solutions</li>
                    <li>IoT Consulting Services</li>
                    <li>24/7 Technical Support</li>
                </ul>
                <h3>Why Choose Us?</h3>
                <p>With years of experience and a team of dedicated professionals, we offer unparalleled expertise
                     and support to ensure your IoT projects are successful. Our solutions are designed to be scalable,
                      secure, and user-friendly, making us the preferred choice for IoT needs.</p>
            </div>
    
            </div>

        </div>

    )
}


export default About;