import { render, screen, waitFor, fireEvent } from '@testing-library/react'
import * as token from '../domain/token'
import * as authService from '../api/authService'
import { AuthProvider, useAuth } from './AuthContext'

function AuthConsumer() {
  const { user, isLoading, login, logout } = useAuth()
  if (isLoading) return <div data-testid="auth-status">loading</div>
  return (
    <div>
      <div data-testid="auth-status">{user ? 'logged-in' : 'logged-out'}</div>
      {user && <div data-testid="user-email">{user.email}</div>}
      <button onClick={() => login('u@t.com', 'pw')}>Login</button>
      <button onClick={logout}>Logout</button>
    </div>
  )
}

it('should_be_logged_out_when_no_token_in_localStorage', async () => {
  vi.spyOn(token, 'retrieveToken').mockReturnValue(null)
  render(<AuthProvider><AuthConsumer /></AuthProvider>)
  await waitFor(() => expect(screen.getByTestId('auth-status')).toHaveTextContent('logged-out'))
})

it('should_restore_session_from_valid_stored_token', async () => {
  const payload = btoa(JSON.stringify({ exp: 9999999999 }))
  vi.spyOn(token, 'retrieveToken').mockReturnValue(`h.${payload}.s`)
  vi.spyOn(authService, 'getMe').mockResolvedValue({ user_id: 1, email: 'u@t.com' })
  render(<AuthProvider><AuthConsumer /></AuthProvider>)
  await waitFor(() => expect(screen.getByTestId('user-email')).toHaveTextContent('u@t.com'))
})

it('should_remove_expired_token_on_mount', async () => {
  const payload = btoa(JSON.stringify({ exp: 1 }))
  vi.spyOn(token, 'retrieveToken').mockReturnValue(`h.${payload}.s`)
  const removeSpy = vi.spyOn(token, 'removeToken')
  render(<AuthProvider><AuthConsumer /></AuthProvider>)
  await waitFor(() => expect(screen.getByTestId('auth-status')).toHaveTextContent('logged-out'))
  expect(removeSpy).toHaveBeenCalledOnce()
})

it('should_store_token_and_set_user_on_login', async () => {
  vi.spyOn(token, 'retrieveToken').mockReturnValue(null)
  vi.spyOn(authService, 'login').mockResolvedValue({ access_token: 'new.tok' })
  vi.spyOn(authService, 'getMe').mockResolvedValue({ user_id: 1, email: 'u@t.com' })
  const storeSpy = vi.spyOn(token, 'storeToken')
  render(<AuthProvider><AuthConsumer /></AuthProvider>)
  await waitFor(() => expect(screen.getByTestId('auth-status')).toHaveTextContent('logged-out'))
  fireEvent.click(screen.getByText('Login'))
  await waitFor(() => expect(screen.getByTestId('user-email')).toHaveTextContent('u@t.com'))
  expect(storeSpy).toHaveBeenCalledWith('new.tok')
})

it('should_remove_token_and_clear_user_on_logout', async () => {
  const payload = btoa(JSON.stringify({ exp: 9999999999 }))
  vi.spyOn(token, 'retrieveToken').mockReturnValue(`h.${payload}.s`)
  vi.spyOn(authService, 'getMe').mockResolvedValue({ user_id: 1, email: 'u@t.com' })
  const removeSpy = vi.spyOn(token, 'removeToken')
  render(<AuthProvider><AuthConsumer /></AuthProvider>)
  await waitFor(() => expect(screen.getByTestId('user-email')).toHaveTextContent('u@t.com'))
  fireEvent.click(screen.getByText('Logout'))
  await waitFor(() => expect(screen.getByTestId('auth-status')).toHaveTextContent('logged-out'))
  expect(removeSpy).toHaveBeenCalled()
})
