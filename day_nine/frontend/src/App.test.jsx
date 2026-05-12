import { render, screen, waitFor } from '@testing-library/react'
import * as token from './domain/token'
import App from './App'

it('should_redirect_to_login_when_unauthenticated_user_visits_dashboard', async () => {
  vi.spyOn(token, 'retrieveToken').mockReturnValue(null)
  render(<App />)
  await waitFor(() => expect(screen.getByLabelText(/email/i)).toBeInTheDocument())
})
