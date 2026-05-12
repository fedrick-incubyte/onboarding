import { renderHook } from '@testing-library/react'
import * as taskService from '../api/taskService'
import { useTasks } from './useTasks'

it('should_start_in_loading_state', () => {
  vi.spyOn(taskService, 'getTasks').mockResolvedValue([])
  const { result } = renderHook(() => useTasks())
  expect(result.current.isLoading).toBe(true)
})
