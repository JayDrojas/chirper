import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { RandomTweets } from "./utils";

const Recent = () => {
  const tweets = useSelector(store => Object.values(store.tweets))
  const user = useSelector(store => store.session.user)
  const randomTweets = RandomTweets(tweets, user)

  return (
    <div className="happening-div">
      <div className="right-div-title">
        <h3>What's happening</h3>
      </div>
      <div>
        <div id="right-tweet-content" className="each-tweet-right">
          <h4>Damian Rojas</h4>
          <p>My name is Damian and I created this twitter clone below are links to LinkedIn and github.</p>
        </div>
        {randomTweets && randomTweets.map(tweet => (
          <Link className="link-tags" key={tweet.id} to={`/chirps/${tweet.id}`}>
            <div className="each-tweet-right">
              <h4>{tweet.user.username}</h4>
              <p>{tweet.content.length > 55 ? tweet.content.slice(0, 55) + "...": tweet.content}</p>
            </div>
          </Link>
        ))}
      </div>
      <div className="right-div-title">
        Thank you for visiting!
      </div>
    </div>
  )
}

export default Recent;
