import { ModalContext } from "../../../context/Modal";
import { loadFollowings, getUser } from "../../../store/user";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState, useContext } from "react";
import { Link } from "react-router-dom";
import "./FollowingSneakPeak.css";
import UserCard from "../FollowersModal/UserCard";

const FollowingSneakPeak = ({ userId }) => {
  const dispatch = useDispatch();
  const { modalType, setModalType } = useContext(ModalContext);
  let user = useSelector((state) => state.user.singleUser);
  const followings = useSelector((state) => state.user.userList.Followings);
  const [isLoaded, setIsLoaded] = useState(false);
  const [showUserCard, setShowUserCard] = useState(null);

  const showFollowingModal = () => {
    setModalType("Following");
  };

  const handleUserCard = (idx) => {
    setShowUserCard(idx);
  };

  const handleCloseUserCard = () => {
    setShowUserCard(null);
  };

  useEffect(() => {
    dispatch(loadFollowings(userId, "1", "5")).then(() =>
      dispatch(getUser(userId)).then((res) => setIsLoaded(true))
    );
  }, [modalType, userId]);
  if (isLoaded) {
    return (
      <div className="following-peak">
        <h4>Following</h4>
        <div className="following-list">
          {followings.map((following, idx) => {
            if (idx > 5) return;
            return (
              <li key={idx}>
                <div
                  className="follower-item"
                  onMouseLeave={handleCloseUserCard}
                >
                  {showUserCard === idx && (
                    <div className="article-user-card">
                      <UserCard userId={following.id} idx={idx} />
                    </div>
                  )}
                  <div>
                    <a
                      onMouseOver={() => handleUserCard(idx)}
                      href={`/users/${following.id}`}
                      key={`a-${idx}`}
                    >
                      {following.firstName} {following.lastName}
                    </a>
                  </div>
                </div>
              </li>
            );
          })}
        </div>
        <div className="expand-following textBtn">
          <button onClick={showFollowingModal}>
            See all ({user.followingCount})
          </button>
        </div>
      </div>
    );
  } else {
    return <h1>Loading....</h1>;
  }
};

export default FollowingSneakPeak;
