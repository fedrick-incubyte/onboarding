import axios from 'axios'
import { retrieveToken, removeToken } from '../domain/token'

export const apiClient = axios.create({ baseURL: import.meta.env.VITE_API_BASE_URL })

apiClient.interceptors.request.use((config) => {
  const t = retrieveToken()
  if (t) config.headers['Authorization'] = `Bearer ${t}`
  return config
})

apiClient.interceptors.response.use(
  (r) => r,
  (error) => {
    if (error.response?.status === 401) {
      removeToken()
      window.dispatchEvent(new Event('auth:expired'))
    }
    return Promise.reject(error)
  }
)
