import { apiClient } from './axiosInstance'

it('should_use_VITE_API_BASE_URL', () => {
  expect(apiClient.defaults.baseURL).toBe(import.meta.env.VITE_API_BASE_URL)
})
