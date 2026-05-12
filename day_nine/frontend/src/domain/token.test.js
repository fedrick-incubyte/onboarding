import { storeToken } from './token'

it('should_store_token_in_localStorage', () => {
  storeToken('my.jwt.token')
  expect(localStorage.getItem('auth_token')).toBe('my.jwt.token')
})
