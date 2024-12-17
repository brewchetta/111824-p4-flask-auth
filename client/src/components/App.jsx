import { useState, useEffect } from 'react'
import UserPanel from "./UserPanel"
import Notes from "./Notes"

function App() {

  // STATE //

  const [currentUser, setCurrentUser] = useState(null)
  // we'll partially track the signed in user using state

  async function checkSession() {
    const response = await fetch('/api/check_session')
    if (response.status === 200) {
      const data = await response.json()
      setCurrentUser(data)
    }
  }

  useEffect(() => {
    checkSession()
  }, [])


  // RENDER //

  return (
    <div className="App">

      <h1>Authentication + Authorization</h1>

      <UserPanel currentUser={currentUser} setCurrentUser={setCurrentUser} />

      <Notes />

    </div>
  );
}

export default App;
