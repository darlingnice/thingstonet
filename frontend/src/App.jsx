import Home from "./pages/Home/Home";
import { BrowserRouter,Routes,Route } from "react-router-dom";
import { PublicRoutes  } from "./routes/PublicRoutes";
const App =()=>{
  return (
    <>
      <BrowserRouter>
        <PublicRoutes/>
      
      </BrowserRouter>
    </>
  )
}
export default App;