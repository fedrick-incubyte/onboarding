import MockAdapter from 'axios-mock-adapter'
import { apiClient } from './axiosInstance'
import { login } from './authService'

const mock = new MockAdapter(apiClient)
afterEach(() => mock.reset())

it('should_post_credentials_to_login_endpoint', async () => {
  mock.onPost('/login').reply(200, { access_token: 'tok', token_type: 'bearer', expires_in: 3600 })
  expect(await login('u@t.com', 'pw')).toMatchObject({ access_token: 'tok' })
})
