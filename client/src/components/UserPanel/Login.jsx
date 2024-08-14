import { useState } from 'react'

function Login({ setCurrentUser }) {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  // SUBMIT EVENT

  function handleSubmit(e) {
    e.preventDefault()

    console.log("Please write code here to attempt login...")
  }

  // RENDER //

  return (
    <form className='user-form' onSubmit={handleSubmit}>

      <h2>Login</h2>

      <input type="text"
      onChange={e => setUsername(e.target.value)}
      value={username}
      placeholder='username'
      />

      <input type="text"
      onChange={e => setPassword(e.target.value)}
      value={password}
      placeholder='password'
      />

      <input type="submit"
      value='Login'
      />

    </form>
  )

}

export default Login
