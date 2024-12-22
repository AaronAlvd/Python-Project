import { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { FaUserCircle } from 'react-icons/fa';
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../Login/LoginFormModal";
import SignupFormModal from "../Signup/SignupFormModal";

function ProfileButton() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((store) => store.session.user);
  const ulRef = useRef();

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const logout = (e) => {
    e.preventDefault();
    dispatch(thunkLogout());
    closeMenu();
  };

  return (
    <>
        <FaUserCircle onClick={toggleMenu} style={{fontSize: 34, padding: 5}}/>
      {showMenu && (
        <ul className={"profile-dropdown"} ref={ulRef}>
          {user ? (
            <>
              <li className="ProfileButton-lists" onClick={() => navigate('/profile')}>Profile</li>
              <li className="ProfileButton-lists" onClick={logout}>Log Out</li>
            </>
          ) : (
            <>
              <p className="ProfileButton-lists">
                <OpenModalMenuItem itemText="Log In" onItemClick={closeMenu} modalComponent={<LoginFormModal />} />
              </p>
              <p className="ProfileButton-lists">
                <OpenModalMenuItem itemText="Sign Up" onItemClick={closeMenu} modalComponent={<SignupFormModal />} />
              </p>
            </>
          )}
        </ul>
      )}
    </>
  );
}

export default ProfileButton;
