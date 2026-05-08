import { Toggle } from './ui/Toggle.jsx'

export function DarkModeToggle({ darkMode, onToggle }) {
  return (
    <div className="flex items-center gap-2">
      <span className="text-sm text-slate-500 dark:text-slate-400">{darkMode ? '🌙' : '☀️'}</span>
      <Toggle checked={darkMode} onToggle={onToggle} />
    </div>
  )
}
