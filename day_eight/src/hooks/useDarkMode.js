import { useState } from 'react'

export function useDarkMode() {
  const [darkMode, setDarkMode] = useState(false)
  return [darkMode, () => setDarkMode(d => !d)]
}
