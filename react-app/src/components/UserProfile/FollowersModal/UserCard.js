import "./UserCard.css";
import { useState, useEffect } from "react";
import { getPopupUser } from "../../../store/user";
import { useDispatch, useSelector } from "react-redux";
import FollowButton from "../FollowButton";

const UserCard = ({ userId }) => {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  // let user = useSelector((state) => {
  //   let single = state.user.singleUser;
  //   if (single.id === userId) {
  //     return single;
  //   }
  //   let [filtered] = state.user.userList.Followings.filter(
  //     (following) => following.id === userId
  //   );
  //   return filtered;
  // });
  let user = useSelector((state) => state.user.popupUser);

  useEffect(() => {
    dispatch(getPopupUser(userId)).then((res) => setIsLoaded(true));
  }, []);

  if (isLoaded) {
    return (
      <div className="user-card">
        <div className="card-header">
          <a href={`/users/${user.id}`}>
            <h2>
              {user.firstName} {user.lastName}
            </h2>
          </a>
        </div>
        <div className="card-content">{user.bio}</div>
        <div className="card-sep"></div>
        <div className="card-footer">
          <div className="card-follower-count">
            {user.followerCount} Followers
          </div>
          <div className="btn">
            <FollowButton userId={user.id} key={null} noDispatch={true} />
            {/* <button>Follow</button> */}
          </div>
        </div>
      </div>
    );
  }
  return <div className="loading-popup"></div>;
};

export default UserCard;
