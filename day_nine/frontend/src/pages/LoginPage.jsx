import { useState, useContext } from 'react'
import { AuthContext } from '../context/AuthContext'

export default function LoginPage() {
  const { login } = useContext(AuthContext)
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    await login(email, password)
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">Email</label>
      <input id="email" type="email" value={email} onChange={e => setEmail(e.target.value)} />
      <label htmlFor="password">Password</label>
      <input id="password" type="password" value={password} onChange={e => setPassword(e.target.value)} />
      <button type="submit">Sign in</button>
    </form>
  )
}
