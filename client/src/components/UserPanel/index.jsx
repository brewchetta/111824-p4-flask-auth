import Signup from './Signup'
import Login from './Login'
import UserDetails from "./UserDetails"

function UserPanel({currentUser, setCurrentUser}) {

  // RENDER //

  if (!currentUser) { // Signup & Login if no currentUser

    return (
        
        <div className="flex-row">

          <Signup setCurrentUser={setCurrentUser} />

          <Login setCurrentUser={setCurrentUser} />

        </div>
    
    )

    } else { // UserDetails if currentUser
      
      return (
        <UserDetails currentUser={currentUser} setCurrentUser={setCurrentUser} />
      )

    }

}

export default UserPanel
