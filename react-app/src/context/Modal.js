import React, { useContext, useRef, useState, useEffect } from "react";
import "./Modal.css";
import LoginForm from "../components/auth/LoginForm";
import SignUpForm from "../components/auth/SignUpForm";
import FollowersModal from "../components/UserProfile/FollowersModal/FollowersModal";
import FollowingModal from "../components/UserProfile/FollowersModal/FollowingModal";
export const ModalContext = React.createContext();

export function ModalProvider({ children }) {
  const modalRef = useRef();
  const [value, setValue] = useState();
  const [modalType, setModalType] = useState(null);

  useEffect(() => {
    setValue(modalRef.current);
  }, []);

  return (
    <>
      <ModalContext.Provider value={{ value, modalType, setModalType }}>
        {children}
      </ModalContext.Provider>
      <div ref={modalRef} />
    </>
  );
}

export function SelectedModals() {
  const { modalType, setModalType } = useContext(ModalContext);
  if (modalType === "Login") {
    return (
      <div className="modal">
        <LoginForm />
        <div
          onClick={() => setModalType(null)}
          className="modal-background"
        ></div>
      </div>
    );
  }
  if (modalType === "Signup") {
    return (
      <div className="modal">
        <SignUpForm />
        <div
          onClick={() => setModalType(null)}
          className="modal-background"
        ></div>
      </div>
    );
  }
  if (modalType == "Followers") {
    return (
      <div className="modal">
        <FollowersModal />
        <div
          onClick={() => setModalType(null)}
          className="modal-background follow-background"
        ></div>
      </div>
    );
  }
  if (modalType == "Following") {
    return (
      <div className="modal">
        <FollowingModal />
        <div
          onClick={() => setModalType(null)}
          className="modal-background follow-background"
        ></div>
      </div>
    );
  }

  return null;
}
