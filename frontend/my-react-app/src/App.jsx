import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Elon Tweet Analysis</h1>
      <h2>Making stock predictions based off the things Elon says</h2>
      <div class="column-container">
        <div class="column">
          <div class="displayer">
            <h2>Most Recent Tweet</h2>
          </div>
        </div>
        <div class="column">
          <div class="displayer">
            <h2>Recommendations</h2>
          </div>
        </div>
      </div>
      <div class="displayer">
        <h2>Last 100 Tweets</h2>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App