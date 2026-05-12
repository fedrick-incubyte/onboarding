import { apiClient } from './axiosInstance'

export async function login(email, password) {
  const r = await apiClient.post('/login', { email, password })
  return r.data
}

export async function register(email, password) {
  const r = await apiClient.post('/register', { email, password })
  return r.data
}

export async function getMe() {
  const r = await apiClient.get('/me')
  return r.data
}
