import { apiClient } from './axiosInstance'

export async function getTasks() {
  const r = await apiClient.get('/tasks')
  return r.data
}

export async function createTask(data) {
  const r = await apiClient.post('/tasks', data)
  return r.data
}

export async function updateTask(id, data) {
  const r = await apiClient.put(`/tasks/${id}`, data)
  return r.data
}

export async function deleteTask(id) {
  await apiClient.delete(`/tasks/${id}`)
}
