const TOKEN_KEY = 'auth_token'

export function storeToken(token) {
  localStorage.setItem(TOKEN_KEY, token)
}
