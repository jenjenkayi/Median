import { followThunk, followsUser, unfollowThunk } from "../../../store/user";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState, useContext } from "react";
import { ModalContext } from "../../../context/Modal";
import "./FollowListUser.css";
import FollowButton from "../FollowButton";

const FollowListUser = ({ user, idx }) => {
  const dispatch = useDispatch();
  const currentUser = useSelector((state) => state.session.user);
  const [isFollowing, setIsFollowing] = useState(false);
  const { setModalType } = useContext(ModalContext);

  // useEffect(() => {
  //   followsUser(user.id).then((res) => setIsFollowing(res));
  // }, []);

  // const handleFollow = () => {
  //   if (!currentUser) {
  //     setModalType("Login");
  //     return;
  //   }
  //   dispatch(followThunk(user.id))
  //     .then(() => followsUser(user.id))
  //     .then((res) => setIsFollowing(res));
  // };

  // const handleUnfollow = () => {
  //   dispatch(unfollowThunk(user.id))
  //     .then(() => followsUser(user.id))
  //     .then((res) => setIsFollowing(res));
  // };

  return (
    <div key={`main-${idx}`} className="follow-user">
      <li key={idx}>
        <div className="follow-right-container">
          {/* <div>{user.id}</div> */}
          <div className="follow-info">
            <a href={`/users/${user.id}`}>
              <div className="follow-name">
                {user.firstName} {user.lastName}
              </div>
            </a>
            <div className="follow-bio" key={idx}>
              {user.bio}
            </div>
          </div>
        </div>
        {/* <div className="action-btns">
          {isFollowing && currentUser && user.id != currentUser.id && (
            <button className="unfollow" key={idx} onClick={handleUnfollow}>
              Unfollow
            </button>
          )}
          {!isFollowing && currentUser && user.id != currentUser.id && (
            <button className="follow-btn" onClick={handleFollow} key={idx}>
              Follow
            </button>
          )}
          {!currentUser && (
            <button className="follow-btn" onClick={handleFollow} key={idx}>
              Follow
            </button>
          )}
        </div> */}
        <FollowButton userId={user.id} idx={idx} />
      </li>
    </div>
  );
};

export default FollowListUser;
