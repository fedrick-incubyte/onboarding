import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { AuthContext } from '../context/AuthContext'
import LoginPage from './LoginPage'

const mockNavigate = vi.fn()
vi.mock('react-router-dom', async () => ({
  ...(await vi.importActual('react-router-dom')),
  useNavigate: () => mockNavigate,
}))

function wrapper({ children }) {
  return <AuthContext.Provider value={{ login: vi.fn(), isLoading: false }}>{children}</AuthContext.Provider>
}

it('should_render_email_and_password_fields', () => {
  render(<LoginPage />, { wrapper })
  expect(screen.getByLabelText(/email/i)).toBeInTheDocument()
  expect(screen.getByLabelText(/password/i)).toBeInTheDocument()
})

it('should_call_login_and_redirect_to_dashboard_on_submit', async () => {
  const mockLogin = vi.fn().mockResolvedValue(undefined)
  render(<LoginPage />, { wrapper: ({ children }) => <AuthContext.Provider value={{ login: mockLogin }}>{children}</AuthContext.Provider> })
  await userEvent.type(screen.getByLabelText(/email/i), 'u@t.com')
  await userEvent.type(screen.getByLabelText(/password/i), 'pw123')
  await userEvent.click(screen.getByRole('button', { name: /sign in/i }))
  expect(mockLogin).toHaveBeenCalledWith('u@t.com', 'pw123')
  expect(mockNavigate).toHaveBeenCalledWith('/dashboard')
})

it('should_display_error_message_on_failed_login', async () => {
  const mockLogin = vi.fn().mockRejectedValue(new Error('Invalid credentials'))
  render(<LoginPage />, { wrapper: ({ children }) => <AuthContext.Provider value={{ login: mockLogin }}>{children}</AuthContext.Provider> })
  await userEvent.click(screen.getByRole('button', { name: /sign in/i }))
  expect(await screen.findByText(/invalid credentials/i)).toBeInTheDocument()
})

it('should_disable_submit_button_while_logging_in', async () => {
  let resolve
  const mockLogin = vi.fn().mockReturnValue(new Promise(r => { resolve = r }))
  render(<LoginPage />, { wrapper: ({ children }) => <AuthContext.Provider value={{ login: mockLogin }}>{children}</AuthContext.Provider> })
  await userEvent.click(screen.getByRole('button', { name: /sign in/i }))
  expect(screen.getByRole('button', { name: /sign in/i })).toBeDisabled()
  resolve()
})
