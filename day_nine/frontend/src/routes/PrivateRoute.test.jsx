import { render, screen } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'
import PrivateRoute from './PrivateRoute'

function renderWithAuth(authValue) {
  return render(
    <AuthContext.Provider value={authValue}>
      <MemoryRouter initialEntries={['/dashboard']}>
        <Routes>
          <Route path="/login" element={<div>Login Page</div>} />
          <Route path="/dashboard" element={<PrivateRoute><div>Dashboard Content</div></PrivateRoute>} />
        </Routes>
      </MemoryRouter>
    </AuthContext.Provider>
  )
}

it('should_render_children_when_user_is_authenticated', () => {
  renderWithAuth({ isAuthenticated: true, isLoading: false })
  expect(screen.getByText('Dashboard Content')).toBeInTheDocument()
})

it('should_redirect_to_login_when_not_authenticated', () => {
  renderWithAuth({ isAuthenticated: false, isLoading: false })
  expect(screen.getByText('Login Page')).toBeInTheDocument()
})

it('should_render_nothing_while_auth_is_loading', () => {
  renderWithAuth({ isAuthenticated: false, isLoading: true })
  expect(screen.queryByText('Dashboard Content')).not.toBeInTheDocument()
  expect(screen.queryByText('Login Page')).not.toBeInTheDocument()
})
