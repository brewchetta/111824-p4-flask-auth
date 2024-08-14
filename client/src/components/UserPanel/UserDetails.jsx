function UserDetails({currentUser, setCurrentUser}) {

  function handleLogout() {
    setCurrentUser(null) // set current user to null to clear them out of state
    console.log("Please write code here to attempt logout...")
  }

    return (
      <div className='user-details'>
        <h2>Welcome {currentUser.username}!</h2>
        <button onClick={handleLogout}>Logout</button>
      </div>
    )
  
  }
  
  export default UserDetails
  