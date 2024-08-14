import { useState, useEffect } from 'react'
import UserPanel from "./UserPanel"
import Notes from "./Notes"

function App() {

  // STATE //

  const [currentUser, setCurrentUser] = useState(null) 
  // we'll partially track the signed in user using state

  const [loading, setLoading] = useState(true)


  // EFFECTS //

  useEffect(() => {
    fetch('/api/check_session')
    .then(res => {
      setLoading(false)
      if (res.status === 200) {
        res.json()
        .then(data => setCurrentUser(data))
      }
    })
  }, [])

  // RENDER //

  if (loading) {
    return <h1>LOADING.....</h1>
  }

  return (
    <div className="App">

      <h1>Authentication + Authorization</h1>

      <UserPanel currentUser={currentUser} setCurrentUser={setCurrentUser} />

      <Notes />

    </div>
  );
}

export default App;
