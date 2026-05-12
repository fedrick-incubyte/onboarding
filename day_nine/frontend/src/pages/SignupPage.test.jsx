import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { AuthContext } from '../context/AuthContext'
import * as authService from '../api/authService'
import SignupPage from './SignupPage'

function wrapper({ children }) {
  return <AuthContext.Provider value={{ login: vi.fn() }}>{children}</AuthContext.Provider>
}

it('should_render_email_and_password_fields', () => {
  render(<SignupPage />, { wrapper })
  expect(screen.getByLabelText(/email/i)).toBeInTheDocument()
  expect(screen.getByLabelText(/password/i)).toBeInTheDocument()
})

it('should_call_register_then_login_on_submit', async () => {
  const mockRegister = vi.spyOn(authService, 'register').mockResolvedValue({})
  const mockLogin = vi.fn().mockResolvedValue(undefined)
  render(<SignupPage />, { wrapper: ({ children }) => <AuthContext.Provider value={{ login: mockLogin }}>{children}</AuthContext.Provider> })
  await userEvent.type(screen.getByLabelText(/email/i), 'u@t.com')
  await userEvent.type(screen.getByLabelText(/password/i), 'pw123')
  await userEvent.click(screen.getByRole('button', { name: /sign up/i }))
  expect(mockRegister).toHaveBeenCalledWith('u@t.com', 'pw123')
  expect(mockLogin).toHaveBeenCalledWith('u@t.com', 'pw123')
})

it('should_display_error_message_on_failed_signup', async () => {
  vi.spyOn(authService, 'register').mockRejectedValue(new Error('Email already registered'))
  render(<SignupPage />, { wrapper })
  await userEvent.click(screen.getByRole('button', { name: /sign up/i }))
  expect(await screen.findByText(/email already registered/i)).toBeInTheDocument()
})
