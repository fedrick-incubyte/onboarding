import { Toggle } from './ui/Toggle.jsx'

export function DarkModeToggle({ darkMode, onToggle }) {
  return <Toggle checked={darkMode} onToggle={onToggle} />
}
