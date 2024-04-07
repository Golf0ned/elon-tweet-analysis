import React, { useState, useEffect} from 'react'
import './App.css'
import { initializeApp } from "firebase/app";
import { ref, onValue, getDatabase } from "firebase/database";
import 'firebase/database';

const firebaseConfig = {
  apiKey: "AIzaSyBth9GJ1ig1dLcgxubtwzG3vuoocJJmjDo",
  authDomain: "elon-tweet-analysis.firebaseapp.com",
  databaseURL: "https://elon-tweet-analysis-default-rtdb.firebaseio.com",
  projectId: "elon-tweet-analysis",
  storageBucket: "elon-tweet-analysis.appspot.com",
  messagingSenderId: "362434812086",
  appId: "1:362434812086:web:582d32a5607d69e0f76e17",
  measurementId: "G-ND78YWVZGS"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

function App() {
  const [data, setData] = useState(null)
  
  useEffect(() => {
    const database = getDatabase(app);
    const dbref = ref(database, '/');

    onValue(dbref, (snapshot) => {
      setData(snapshot.val());
    });
  }, []);

  return (
    <>
      <h1>Elon Tweet Analysis</h1>
      <h2>Making stock predictions based off the things Elon says</h2>
      <div class="column-container">
        <div class="column">
          <div class="displayer">
            <h2>Most Recent Tweet</h2>
            <div className="scrollable-container">
              <div className="scrollable-content">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at risus neque. Integer euismod orci a libero rhoncus facilisis. Duis convallis convallis tellus, eu semper ipsum tincidunt eget. In turpis augue, vestibulum ac augue et, consequat aliquet risus. Quisque ac urna et velit ornare scelerisque. Suspendisse potenti. Proin id libero mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum commodo nulla eu augue fringilla tristique. Ut volutpat malesuada libero, non gravida arcu euismod eu. Quisque eget urna vel erat ullamcorper varius. Etiam malesuada velit bibendum mi bibendum, sit amet mollis dolor vestibulum. Proin vitae elit non felis placerat ultricies. Cras tempor quam a mollis varius. Cras semper risus vel purus convallis, in posuere ipsum tempor.</p>
                <p>Integer pharetra enim id lectus euismod posuere. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque auctor justo quis orci facilisis aliquet. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam et diam ac quam tincidunt interdum. In hac habitasse platea dictumst. Sed ut enim ac quam posuere lacinia. Ut at lorem elit. Donec pretium non arcu ut bibendum. Donec convallis ligula et venenatis dapibus. Sed nec semper metus. Sed in nisi malesuada, tempus arcu non, consequat lorem. Ut lacinia pretium libero, nec pretium purus venenatis nec. Nullam accumsan, nunc id scelerisque lobortis, felis risus varius orci, eget ultrices dolor nisi quis dui. Donec nec tellus magna. Suspendisse potenti.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="column">
          <div class="displayer">
            <h2>Recommendations</h2>
            <div className="scrollable-container">
              <div className="scrollable-content">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at risus neque. Integer euismod orci a libero rhoncus facilisis. Duis convallis convallis tellus, eu semper ipsum tincidunt eget. In turpis augue, vestibulum ac augue et, consequat aliquet risus. Quisque ac urna et velit ornare scelerisque. Suspendisse potenti. Proin id libero mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum commodo nulla eu augue fringilla tristique. Ut volutpat malesuada libero, non gravida arcu euismod eu. Quisque eget urna vel erat ullamcorper varius. Etiam malesuada velit bibendum mi bibendum, sit amet mollis dolor vestibulum. Proin vitae elit non felis placerat ultricies. Cras tempor quam a mollis varius. Cras semper risus vel purus convallis, in posuere ipsum tempor.</p>
                <p>Integer pharetra enim id lectus euismod posuere. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque auctor justo quis orci facilisis aliquet. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam et diam ac quam tincidunt interdum. In hac habitasse platea dictumst. Sed ut enim ac quam posuere lacinia. Ut at lorem elit. Donec pretium non arcu ut bibendum. Donec convallis ligula et venenatis dapibus. Sed nec semper metus. Sed in nisi malesuada, tempus arcu non, consequat lorem. Ut lacinia pretium libero, nec pretium purus venenatis nec. Nullam accumsan, nunc id scelerisque lobortis, felis risus varius orci, eget ultrices dolor nisi quis dui. Donec nec tellus magna. Suspendisse potenti.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="displayer">
        <h2>Last 100 Tweets</h2>
        <div className="scrollable-container">
          <div className="scrollable-content">
          <div>
            {data.map(tweet) => (
              <div key={tweet.index}>
                <p>{tweet.tweet}</p>
              </div>
            )}
          </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default App