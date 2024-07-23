
import './Slider.css'

export const Slider = ()=>{
    return (
        <>        
            <div class="slider-container">
                 <input type="range" min="1" max="100" value="50" class="slider" id="myRange"></input>
            </div>
        </>
    )
    
}
