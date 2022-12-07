import React, { useContext, useRef, useState, useEffect } from "react";
import "./Modal2.css";
import CreateCommentModal from "../components/CreateCommentModal/CreateCommentForm";
import { useSelector } from "react-redux";

export const ModalContext2 = React.createContext();

export function ModalProvider2({ children }) {
  const modal2Ref = useRef();
  const [value, setValue] = useState();
  const [modalType2, setModalType2] = useState(null);

  useEffect(() => {
    setValue(modal2Ref.current);
  }, []);

  return (
    <>
      <ModalContext2.Provider value={{ value, modalType2, setModalType2 }}>
        {children}
      </ModalContext2.Provider>
      <div ref={modal2Ref} />
    </>
  );
}

export function SelectedModals2() {
  const { modalType2, setModalType2 } = useContext(ModalContext2);
  const story = useSelector((state) => state.story.singleStory);

  if (modalType2 === "comments") {
    return (
      <div className="modal2">
        <CreateCommentModal story={story} />
        <div
          onClick={() => setModalType2(null)}
          className="modal2-background"
        ></div>
      </div>
    );
  }

  return null;
}
