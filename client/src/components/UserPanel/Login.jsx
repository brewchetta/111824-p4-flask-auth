import { useState } from 'react'

function Login({ setCurrentUser }) {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  // SUBMIT EVENT

  async function handleSubmit(e) {
    e.preventDefault()

    const response = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ username, password })
    })

    if (response.ok) {
      const user = await response.json()
      setCurrentUser( user )
    } else {
      alert("Invalid username or password")
    }
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
