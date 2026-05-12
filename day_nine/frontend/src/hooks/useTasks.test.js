import { renderHook, waitFor } from '@testing-library/react'
import * as taskService from '../api/taskService'
import { useTasks } from './useTasks'

it('should_start_in_loading_state', () => {
  vi.spyOn(taskService, 'getTasks').mockResolvedValue([])
  const { result } = renderHook(() => useTasks())
  expect(result.current.isLoading).toBe(true)
})

it('should_set_tasks_after_successful_fetch', async () => {
  vi.spyOn(taskService, 'getTasks').mockResolvedValue([{ id: 1, title: 'Buy milk' }])
  const { result } = renderHook(() => useTasks())
  await waitFor(() => expect(result.current.tasks).toHaveLength(1))
})

it('should_set_error_on_fetch_failure', async () => {
  vi.spyOn(taskService, 'getTasks').mockRejectedValue(new Error('Network error'))
  const { result } = renderHook(() => useTasks())
  await waitFor(() => expect(result.current.error).toBeTruthy())
})

it('should_append_task_when_addTask_called', async () => {
  vi.spyOn(taskService, 'getTasks').mockResolvedValue([])
  const { result } = renderHook(() => useTasks())
  await waitFor(() => expect(result.current.isLoading).toBe(false))
  result.current.addTask({ id: 99, title: 'New task' })
  await waitFor(() => expect(result.current.tasks).toHaveLength(1))
})
