import { storeToken, retrieveToken, removeToken, decodeTokenPayload } from './token'

it('should_store_token_in_localStorage', () => {
  storeToken('my.jwt.token')
  expect(localStorage.getItem('auth_token')).toBe('my.jwt.token')
})

it('should_retrieve_stored_token', () => {
  localStorage.setItem('auth_token', 'my.jwt.token')
  expect(retrieveToken()).toBe('my.jwt.token')
})

it('should_return_null_when_no_token_stored', () => {
  expect(retrieveToken()).toBeNull()
})

it('should_remove_token_from_localStorage', () => {
  localStorage.setItem('auth_token', 'my.jwt.token')
  removeToken()
  expect(localStorage.getItem('auth_token')).toBeNull()
})

it('should_decode_valid_jwt_payload', () => {
  const payload = btoa(JSON.stringify({ user_id: 1, exp: 9999999999 }))
  expect(decodeTokenPayload(`header.${payload}.sig`)).toMatchObject({ user_id: 1 })
})
