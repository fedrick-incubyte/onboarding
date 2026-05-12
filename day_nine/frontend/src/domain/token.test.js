import { storeToken, retrieveToken, removeToken, decodeTokenPayload, isTokenExpired } from './token'

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

it('should_return_null_for_malformed_token', () => {
  expect(decodeTokenPayload('not-a-token')).toBeNull()
})

it('should_return_true_when_exp_is_in_the_past', () => {
  const payload = btoa(JSON.stringify({ exp: 1 }))
  expect(isTokenExpired(`header.${payload}.sig`)).toBe(true)
})
