import '@testing-library/jest-dom'

const storage = {}
const localStorageMock = {
  getItem: (key) => storage[key] ?? null,
  setItem: (key, value) => { storage[key] = String(value) },
  removeItem: (key) => { delete storage[key] },
  clear: () => { Object.keys(storage).forEach((k) => delete storage[k]) },
}
vi.stubGlobal('localStorage', localStorageMock)

beforeEach(() => {
  localStorageMock.clear()
})
