import {Routes,Route } from 'react-router-dom'
import Home from '../pages/Home/Home'
import About from '../pages/About/About'
import { LoginPage } from '../pages/LoginPage/LoginPage'
import { SignUp } from '../pages/Signup/Signup'
import Services from '../pages/Services/Services'
import { ForgotPassword } from '../pages/ForgotPassword/ForgotPassword'


export const PublicRoutes = ()=>{
    return (
        <Routes>
            <Route index element={<Home/>}/>  
            <Route path='/auth/about' element={<About/>}/>
            <Route path='/auth/services' element={<Services/>}/>
            <Route path='/auth/signup' element={<SignUp/>}/>
            <Route path='/auth/login' element={<LoginPage/>} />
            <Route path='/auth/forgot-pass' element={<ForgotPassword/>} />
        </Routes> 
    )
}