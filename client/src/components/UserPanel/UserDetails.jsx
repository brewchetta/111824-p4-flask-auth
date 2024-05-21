function UserDetails({currentUser, setCurrentUser}) {

    return (
      <div className='user-details'>
        <h2>Welcome {currentUser.username}!</h2>
        <button onClick={() => setCurrentUser(null)}>Logout</button>
      </div>
    )
  
  }
  
  export default UserDetails
  