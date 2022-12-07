import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { getUsersStories } from "../../../store/story";
import UserCard from "../FollowersModal/UserCard";

import "./MoreArticles.css";

const MoreArticles = ({ userId }) => {
  const dispatch = useDispatch();
  const storiesRaw = useSelector((state) => state.story.allStories);
  const [isLoaded, setIsLoaded] = useState(false);
  const stories = Object.values(storiesRaw);
  const [showUserCard, setShowUserCard] = useState(null);

  useEffect(() => {
    dispatch(getUsersStories(userId)).then(() => setIsLoaded(true));
  }, []);

  const handleUserCard = (idx) => {
    setShowUserCard(idx);
  };
  const handleCloseUserCard = () => {
    setShowUserCard(null);
  };

  if (isLoaded) {
    return (
      <div className="more-articles-content">
        <div className="more-articles-title">
          <h4>More from Author</h4>
        </div>
        <div className="article-list" onMouseLeave={handleCloseUserCard}>
          {stories.map((story, idx) => (
            <li key={idx}>
              <div className="article-item">
                <div className="article-user-card">
                  {showUserCard == idx && <UserCard userId={story.author.id} />}
                </div>

                <div className="author" onMouseOver={() => handleUserCard(idx)}>
                  <a href={`/users/${story.author.id}`}>
                    {story.author.firstName} {story.author.lastName}
                  </a>
                </div>
                <div className="title">
                  <a href={`/stories/${story.id}`}>{story.title}</a>
                </div>
              </div>
            </li>
          ))}
        </div>
      </div>
    );
  } else {
    return <h1>Loading....</h1>;
  }
};

export default MoreArticles;
