import { useState, useEffect } from 'react'

export function useLocalStorage(key, initial) {
  const [value, setValue] = useState(initial)
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value))
  }, [key, value])
  return [value, setValue]
}
