import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { AuthContext } from '../context/AuthContext'
import * as taskService from '../api/taskService'
import DashboardPage from './DashboardPage'

const mockAuth = { user: { email: 'u@t.com' }, logout: vi.fn() }
function wrapper({ children }) {
  return <AuthContext.Provider value={mockAuth}>{children}</AuthContext.Provider>
}

it('should_show_loading_state_while_fetching_tasks', () => {
  vi.spyOn(taskService, 'getTasks').mockReturnValue(new Promise(() => {}))
  render(<DashboardPage />, { wrapper })
  expect(screen.getByText(/loading/i)).toBeInTheDocument()
})

it('should_render_task_titles_after_fetch', async () => {
  vi.spyOn(taskService, 'getTasks').mockResolvedValue([{ id: 1, title: 'Buy milk', status: 'todo' }])
  render(<DashboardPage />, { wrapper })
  expect(await screen.findByText('Buy milk')).toBeInTheDocument()
})

it('should_show_error_message_when_fetch_fails', async () => {
  vi.spyOn(taskService, 'getTasks').mockRejectedValue(new Error('Network error'))
  render(<DashboardPage />, { wrapper })
  expect(await screen.findByText(/failed to load tasks/i)).toBeInTheDocument()
})

it('should_display_task_status_badge', async () => {
  vi.spyOn(taskService, 'getTasks').mockResolvedValue([{ id: 1, title: 'Buy milk', status: 'done' }])
  render(<DashboardPage />, { wrapper })
  await screen.findByText('Buy milk')
  expect(screen.getByText('done')).toHaveClass('bg-green-100')
})
