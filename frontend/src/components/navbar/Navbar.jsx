import "./navbar.scss"
import { FiBell } from "react-icons/fi";

const Navbar = () => {
  return (
    <div className='navbar'>
      <div className='wrapper'>
        <div className='items'>
          <div className="item">
            <FiBell className="icon" />
          </div>
          <div className="item">
            Test User Name
          </div>
          <div className="item">
            <img 
            src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png" 
            alt="avatar"
            className="avatar"/>
            
          </div>
        </div>
      </div>
    </div>
  )
}

export default Navbar