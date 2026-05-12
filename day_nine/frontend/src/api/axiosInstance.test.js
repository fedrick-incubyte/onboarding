import axios from 'axios'
import MockAdapter from 'axios-mock-adapter'
import * as token from '../domain/token'
import { apiClient } from './axiosInstance'

const mock = new MockAdapter(apiClient)
afterEach(() => mock.reset())

it('should_use_VITE_API_BASE_URL', () => {
  expect(apiClient.defaults.baseURL).toBe(import.meta.env.VITE_API_BASE_URL)
})

it('should_attach_bearer_token_when_token_exists', async () => {
  vi.spyOn(token, 'retrieveToken').mockReturnValue('fake.jwt.token')
  mock.onGet('/me').reply(200, {})
  const r = await apiClient.get('/me')
  expect(r.config.headers['Authorization']).toBe('Bearer fake.jwt.token')
})

it('should_not_attach_header_when_no_token_exists', async () => {
  vi.spyOn(token, 'retrieveToken').mockReturnValue(null)
  mock.onGet('/me').reply(200, {})
  const r = await apiClient.get('/me')
  expect(r.config.headers['Authorization']).toBeUndefined()
})
