import { render, screen, waitFor } from '@testing-library/react'
import * as token from './domain/token'
import * as authService from './api/authService'
import * as taskService from './api/taskService'
import App from './App'

beforeEach(() => window.history.pushState({}, '', '/'))

it('should_redirect_to_login_when_unauthenticated_user_visits_dashboard', async () => {
  vi.spyOn(token, 'retrieveToken').mockReturnValue(null)
  render(<App />)
  await waitFor(() => expect(screen.getByLabelText(/email/i)).toBeInTheDocument())
})

it('should_show_dashboard_when_authenticated_user_visits_root', async () => {
  const payload = btoa(JSON.stringify({ exp: 9999999999 }))
  vi.spyOn(token, 'retrieveToken').mockReturnValue(`h.${payload}.s`)
  vi.spyOn(authService, 'getMe').mockResolvedValue({ user_id: 1, email: 'u@t.com' })
  vi.spyOn(taskService, 'getTasks').mockResolvedValue([])
  render(<App />)
  await waitFor(() => expect(screen.getByRole('button', { name: /logout/i })).toBeInTheDocument())
})
