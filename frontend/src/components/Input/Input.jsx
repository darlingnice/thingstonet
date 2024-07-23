export const Input = (props)=>{
    return (
        <>
            <input type={props.type} value={props.value} id={props.id} placeholder={props.placeholder} className={props.className} required={props.required}></input>
        </>
    )
}