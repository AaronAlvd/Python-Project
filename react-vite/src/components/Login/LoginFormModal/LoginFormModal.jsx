import { useState } from "react";
import { thunkLogin } from "../../../redux/session";
import { FaUser, FaLock } from 'react-icons/fa';
import { useDispatch } from "react-redux";
import { useModal } from "../../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };

  return (
    <div className="LoginFormModal-div">
      <h1 style={{margin: 0}}>Log In</h1>
        <form onSubmit={handleSubmit} className="LoginFormModal-form">
          <div className="LoginFormModal-div-input">
            <label className="LoginFormModal-label">Email</label>
            <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} required className="LoginFormModal-input"/>
            <FaUser className="LoginFormModal-icon"/>
            {errors.email && <p>{errors.email}</p>}
          </div>

          <div className="LoginFormModal-div-input">
            <label className="LoginFormModal-label">Password</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required className="LoginFormModal-input"/>
            <FaLock className="LoginFormModal-icon"/>
            {errors.password && <p>{errors.password}</p>}
          </div>

          <button type="submit" className="LoginFormModal-button">Log In</button>
        </form>
    </div>
  );
}

export default LoginFormModal;
