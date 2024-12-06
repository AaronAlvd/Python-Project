import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <div className="Navigation-div">
      <NavLink to="/">Home</NavLink>
      <div>
        <ProfileButton />
      </div>
    </div>
  );
}

export default Navigation;
