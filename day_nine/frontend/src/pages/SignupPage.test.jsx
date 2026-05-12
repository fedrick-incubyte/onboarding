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
