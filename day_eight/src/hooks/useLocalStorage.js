import { useState, useEffect } from 'react'

export function useLocalStorage(key, initial) {
  const stored = localStorage.getItem(key)
  const [value, setValue] = useState(stored ? JSON.parse(stored) : initial)
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value))
  }, [key, value])
  return [value, setValue]
}
