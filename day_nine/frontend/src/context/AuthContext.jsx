import { createContext, useContext, useEffect, useState } from 'react'
import { retrieveToken, isTokenExpired, removeToken } from '../domain/token'
import { getMe } from '../api/authService'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    const t = retrieveToken()
    if (!t) { setIsLoading(false); return }
    if (isTokenExpired(t)) { removeToken(); setIsLoading(false); return }
    getMe().then(setUser).finally(() => setIsLoading(false))
  }, [])

  return <AuthContext.Provider value={{ user, isLoading }}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
