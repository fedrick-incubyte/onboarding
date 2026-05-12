import { render, screen, waitFor } from '@testing-library/react'
import * as token from '../domain/token'
import { AuthProvider, useAuth } from './AuthContext'

function AuthConsumer() {
  const { user, isLoading } = useAuth()
  if (isLoading) return <div data-testid="auth-status">loading</div>
  return (
    <div>
      <div data-testid="auth-status">{user ? 'logged-in' : 'logged-out'}</div>
      {user && <div data-testid="user-email">{user.email}</div>}
    </div>
  )
}

it('should_be_logged_out_when_no_token_in_localStorage', async () => {
  vi.spyOn(token, 'retrieveToken').mockReturnValue(null)
  render(<AuthProvider><AuthConsumer /></AuthProvider>)
  await waitFor(() => expect(screen.getByTestId('auth-status')).toHaveTextContent('logged-out'))
})
