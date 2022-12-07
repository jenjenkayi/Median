import React, { useContext, useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { ModalContext } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./login-signup.css";

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [hasSubmitted, setHasSubmitted] = useState(false);

  const dispatch = useDispatch();
  const { setModalType } = useContext(ModalContext);

  const onSignUp = async (e) => {
    setHasSubmitted(true);
    e.preventDefault();
    if (password === repeatPassword) {
      const data = dispatch(
        signUp(username, email, password, firstName, lastName)
      )
        .then((res) => res)
        .then(() => setModalType(null))
        .catch((e) => e.json().then((e) => setErrors(e.errors)));
    }
  };

  useEffect(() => {
    if (password != repeatPassword) {
      setErrors(["Password and Confirm Password must match."]);
    } else {
      setErrors([]);
    }
  }, [password, repeatPassword]);

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  const updateFirstName = (e) => {
    setFirstName(e.target.value);
  };
  const updateLastName = (e) => {
    setLastName(e.target.value);
  };

  // if (user) {
  //   return <Redirect to='/' />;
  // }

  return (
    <form id="signup-container" className="modal-content" onSubmit={onSignUp}>
      <div id="signup-title">Sign Up</div>
      <div id="signup-title-b">Enter below to create an account</div>
      <div className="errors">
        {hasSubmitted && errors.map((error, ind) => <li key={ind}>{error}</li>)}
      </div>
      <label>User Name</label>
      <input
        type="text"
        name="username"
        onChange={updateUsername}
        value={username}
      ></input>
      <label>Email</label>
      <input
        type="text"
        name="email"
        onChange={updateEmail}
        value={email}
      ></input>
      <label>Password</label>
      <input
        type="password"
        name="password"
        onChange={updatePassword}
        value={password}
      ></input>
      <label>Confirm Password</label>
      <input
        type="password"
        name="repeat_password"
        onChange={updateRepeatPassword}
        value={repeatPassword}
        required={true}
      ></input>
      <label>First Name</label>
      <input
        type="text"
        name="first_name"
        onChange={updateFirstName}
        value={firstName}
        required={true}
      ></input>
      <label>Last Name</label>
      <input
        type="text"
        name="rlast_name"
        onChange={updateLastName}
        value={lastName}
        required={true}
      ></input>
      <button type="submit">Sign Up</button>
      <div>
        <div>Already have an Account?</div>
        <div id="login-redirect-signup" onClick={() => setModalType("Login")}>
          Log In Here
        </div>
      </div>
    </form>
  );
};

export default SignUpForm;
