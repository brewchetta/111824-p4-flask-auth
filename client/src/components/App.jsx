import { useState, useEffect } from 'react'
import UserPanel from "./UserPanel"
import Notes from "./Notes"

function App() {

  // STATE //

  const [currentUser, setCurrentUser] = useState(null)
  const [loading, setLoading] = useState(true)
  // we'll partially track the signed in user using state


  // CHECK SESSION //

  useEffect(() => {
    fetch('/api/check_session')
    .then(response => {
      if (response.status === 200) {
        response.json()
        .then(user => setCurrentUser(user))
      }
      setLoading(false)
    })
  }, [])


  // RENDER //

  if (loading) {
    return <h1>Loading...</h1>
  }

  return (
    <div className="App">

      <h1>Authentication + Authorization</h1>

      <UserPanel currentUser={currentUser} setCurrentUser={setCurrentUser} />

      <Notes currentUser={currentUser} />

    </div>
  );
}

export default App;
