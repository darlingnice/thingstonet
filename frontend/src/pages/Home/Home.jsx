import Header from '../../components/Header/Header'
import Maincontent from '../../components/Maincontent/Maincontent';
import Footer from '../../components/Footer/Footer';
import './Home.css'
import { ToggleButton } from '../../components/ToggleButton/ToggleButton';
// import { Slider } from '../../components/Slider/Slider';
import Button from '../../components/Button/Button';
import { Input } from '../../components/Input/Input';
const Home = ()=>{
    return (
        <div className='Home'>
                
                <Header/>
               
                    <ToggleButton/>  
                    <form id='form'>
                        <Input className={"input-field"} id={"email"} placeholder="Enter your email address"/>  
                        <Input className={"input-field"} type={"password"}  id={"password"} placeholder="Enter your password" required={"required"}/>            
                         
                        <Button type={"submit"}  className={'btn-test'} label={"Login"} onclick={()=>{
                            document.getElementById("form").addEventListener("submit",(e)=>{
                                e.preventDefault();
                                const email = document.getElementById("email").value;
                                const password = document.getElementById("password").value;
                            
    
                                console.log(`Your email address is ${email} and your password ${password}`)
                            })
                           
                            
                        }}/>  
                    </form>  
                  
                    
        </div>

    )
}

export default Home;