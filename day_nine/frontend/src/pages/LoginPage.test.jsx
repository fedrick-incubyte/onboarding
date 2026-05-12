import { render, screen } from '@testing-library/react'
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
