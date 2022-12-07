import React, { useContext, useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import { addLikeToStory, getSingleStory } from "../../store/story";
import commentIcon from "../../assets/comment-icon.png";
import likeIcon from "../../assets/like-icon.jpeg";
import "./GetOneStory.css";
import { ModalContext2 } from "../../context/Modal2";
import { ModalContext } from "../../context/Modal";
import UserInfo from "../UserProfile/userSideBar.js/UserInfo";
import MoreArticles from "../UserProfile/userSideBar.js/MoreArticles";
import GetAllStories from "../GetAllStories/GetAllStories";
import profileIcon from "../../assets/profile-icon.jpeg";

const GetOneStory = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { storyId } = useParams();
  const { setModalType2 } = useContext(ModalContext2);
  const { setModalType } = useContext(ModalContext);
  const currentUser = useSelector((state) => state.session.user);
  const story = useSelector((state) => state.story.singleStory);
  const stories = useSelector((state) => state.story.allStories);
  const comment = useSelector((state) => state.comment.singleComment);

  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(getSingleStory(storyId)).then(() => setIsLoaded(true));
  }, [dispatch, storyId, comment]);

  // useEffect(() => {
  //   dispatch(addLikeToStory(storyId, count)).then(() => setIsLoaded(true));
  // }, [dispatch, storyId, count]);

  const handleLike = () => {
    dispatch(addLikeToStory(storyId, 1)).then(() =>
      dispatch(getSingleStory(storyId)).then(() => setIsLoaded(true))
    );
  };
  if (isLoaded) {
    return (
      <div className="containers">
        <div className="story-container2">
          <div className="story-info">
            <div className="story-header">
              <div
                className="story-author-info"
                onClick={() => history.push(`/users/${story.author.id}`)}
              >
                <img
                  className="profile-icon"
                  src={story.author.profile_picture}
                  alt="Profile Icon"
                />{" "}
                {story?.author?.firstName} {story?.author?.lastName}
              </div>
              <div className="story-author-info2">
                {" "}
                {story?.createdAt?.slice(5, 11)}
              </div>
            </div>
            <div className="story-title">{story.title}</div>
            <img className="story-image" src={story.image} alt="" />
            <div className="story-content">{story.content}</div>
            <div className="story-likes-comments">
              <div className="story-likes">
                <img
                  className="like-icon cursor"
                  onClick={handleLike}
                  src={likeIcon}
                  alt="Like Icon"
                />
                <span className="story-like-counts">{story.likeCount}</span>
              </div>
              <div
                className="story-comments"
                onClick={() => {
                  if (currentUser) {
                    setModalType2("comments");
                    return;
                  }
                  setModalType("Login");
                }}
              >
                <img
                  className="comment-icon cursor"
                  src={commentIcon}
                  alt="Comment Icon"
                />
                <span className="story-comment-counts">
                  {story.commentCount}
                </span>
              </div>
            </div>
          </div>
          <div className="get-all-stories">
            <div onClick={() => history.push(`/users/${story.author.id}`)}>
              More from {story?.author?.firstName} {story?.author?.lastName}
            </div>
            <GetAllStories stories={stories} />
          </div>
        </div>

        <div className="container-3">
          <UserInfo userId={story.author.id} />
          <MoreArticles userId={story.author.id} />
        </div>
      </div>
    );
  } else {
    return <h1>Loading...</h1>;
  }
};

export default GetOneStory;
