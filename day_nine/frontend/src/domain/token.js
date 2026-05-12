const TOKEN_KEY = 'auth_token'

export function storeToken(token) {
  localStorage.setItem(TOKEN_KEY, token)
}

export function retrieveToken() {
  return localStorage.getItem(TOKEN_KEY)
}

export function removeToken() {
  localStorage.removeItem(TOKEN_KEY)
}

export function decodeTokenPayload(token) {
  try {
    return JSON.parse(atob(token.split('.')[1]))
  } catch {
    return null
  }
}

export function isTokenExpired(token) {
  const payload = decodeTokenPayload(token)
  return payload === null || payload.exp * 1000 < Date.now()
}
