import React from 'react'
import { useActions, useValues } from 'kea'
import './App.css'
import logic from './app_logic'

function App() {
  const { increment } = useActions(logic)
  const { counter } = useValues(logic)

  return (
    <div className="App">
      <p>Hello, world.</p>
      <p>Clicked { counter } times.</p>
      <button onClick={() => increment(1)}>
        Click me!
      </button>
    </div>
  );
}

export default App;
