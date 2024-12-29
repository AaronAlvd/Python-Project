import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faSearch } from '@fortawesome/free-solid-svg-icons';
import "./Navigation.css";

function Navigation() {
  return (
    <div className="Navigation-div">
      <div className="Navigation-div-navlink">
        <NavLink to="/" className='Navigation-navlink'><h2 className="Navigation-title">WikiDocs</h2></NavLink>
      </div>
      <div className="Navigation-div-profileButton">
        <ProfileButton />
      </div>
    </div>
  );
}

export default Navigation;
