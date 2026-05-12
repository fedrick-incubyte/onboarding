import { apiClient } from './axiosInstance'

export async function getTasks() {
  const r = await apiClient.get('/tasks')
  return r.data
}
