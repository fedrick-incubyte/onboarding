import { useState } from 'react'

export function useLocalStorage(key, initial) {
  const [value, setValue] = useState(initial)
  return [value, setValue]
}
