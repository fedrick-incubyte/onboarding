import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { AuthContext } from '../context/AuthContext'
import LoginPage from './LoginPage'

function wrapper({ children }) {
  return <AuthContext.Provider value={{ login: vi.fn(), isLoading: false }}>{children}</AuthContext.Provider>
}

it('should_render_email_and_password_fields', () => {
  render(<LoginPage />, { wrapper })
  expect(screen.getByLabelText(/email/i)).toBeInTheDocument()
  expect(screen.getByLabelText(/password/i)).toBeInTheDocument()
})

it('should_call_login_on_form_submit', async () => {
  const mockLogin = vi.fn().mockResolvedValue(undefined)
  render(<LoginPage />, { wrapper: ({ children }) => <AuthContext.Provider value={{ login: mockLogin }}>{children}</AuthContext.Provider> })
  await userEvent.type(screen.getByLabelText(/email/i), 'u@t.com')
  await userEvent.type(screen.getByLabelText(/password/i), 'pw123')
  await userEvent.click(screen.getByRole('button', { name: /sign in/i }))
  expect(mockLogin).toHaveBeenCalledWith('u@t.com', 'pw123')
})

it('should_display_error_message_on_failed_login', async () => {
  const mockLogin = vi.fn().mockRejectedValue(new Error('Invalid credentials'))
  render(<LoginPage />, { wrapper: ({ children }) => <AuthContext.Provider value={{ login: mockLogin }}>{children}</AuthContext.Provider> })
  await userEvent.click(screen.getByRole('button', { name: /sign in/i }))
  expect(await screen.findByText(/invalid credentials/i)).toBeInTheDocument()
})
