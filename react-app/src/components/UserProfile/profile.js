import React, { useEffect, useContext, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getUser } from "../../store/user";
import { storyReducer } from "../../store/story";
import UserInfo from "./userSideBar.js/UserInfo";
import "./profile.css";
import { getUsersStories } from "../../store/story";
import GetAllStories from "../GetAllStories/GetAllStories";
import FollowingSneakPeak from "./userSideBar.js/FollowingSneakPeak";
import FollowButton from "./FollowButton";

const Profile = () => {
  const dispatch = useDispatch();
  const { userId } = useParams();

  const user = useSelector((state) => state.user.singleUser);

  const [isLoaded, setIsLoaded] = useState(false);
  const stories = useSelector((state) => state.story.allStories);
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    dispatch(getUser(userId))
      .then(() => dispatch(getUsersStories(userId)))
      .then(() => setIsLoaded(true))
      .catch((e) => e.json())
      .then((e) => setErrors([e]));
  }, [userId]);

  if (isLoaded) {
    return (
      <div className="main">
        <div className="middle-container">
          <div className="header">
            <h1 className="cursor">
              {user.firstName} {user.lastName}
            </h1>
            {/* <div className="sub-nav">Home</div> */}
          </div>
          {/* {user.Stories && (
            <ul>
              {user.Stories.map((story, idx) => {
                return <li key={idx}>{story.title}</li>;
              })}
            </ul>
          )} */}
          <GetAllStories stories={stories} />
        </div>
        <div className="right-container">
          <UserInfo userId={user.id} />
          <FollowingSneakPeak userId={user.id} />
        </div>
      </div>
    );
  }
  if (errors.length) {
    return (
      <div>
        <h2>We're sorry, something went wrong!</h2>
        <ul>
          {errors.map((err, idx) => (
            <li key={idx}>{err.message}</li>
          ))}
        </ul>
      </div>
    );
  }
  return (
    <div>
      <h1>"Loading..."</h1>
    </div>
  );
};

export default Profile;
