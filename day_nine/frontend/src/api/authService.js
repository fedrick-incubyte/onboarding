import { apiClient } from './axiosInstance'

export async function login(email, password) {
  const r = await apiClient.post('/login', { email, password })
  return r.data
}
