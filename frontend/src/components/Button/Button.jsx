import './Button.css'
const Button = (props)=>{
    return <button  type={props.type} className={props.className} onClick={props.onclick}>{props.label}</button>
}

export default Button