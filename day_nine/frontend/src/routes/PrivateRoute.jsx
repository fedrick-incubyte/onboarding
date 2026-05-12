import { useContext } from 'react'
import { AuthContext } from '../context/AuthContext'

export default function PrivateRoute({ children }) {
  const { isAuthenticated } = useContext(AuthContext)
  return children
}
