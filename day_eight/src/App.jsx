import { useState } from 'react'
import { EntryForm } from './components/EntryForm.jsx'
import { EntryGrid } from './components/EntryGrid.jsx'
import { TagFilter } from './components/TagFilter.jsx'
import { DarkModeToggle } from './components/DarkModeToggle.jsx'
import { filterEntries } from './domain/filter.js'
import { useLocalStorage } from './hooks/useLocalStorage.js'
import { useDarkMode } from './hooks/useDarkMode.js'

export default function App() {
  const [entries, setEntries] = useLocalStorage('craftlog-entries', [])
  const [activeTag, setActiveTag] = useState(null)
  const [darkMode, toggleDarkMode] = useDarkMode()

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 text-slate-900 dark:text-slate-100 transition-colors">
      <header className="border-b border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 shadow-sm">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <h1 className="text-2xl font-bold text-brand-500">Craftlog</h1>
          <DarkModeToggle darkMode={darkMode} onToggle={toggleDarkMode} />
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-8 space-y-6">
        <EntryForm onSubmit={entry => setEntries(prev => [entry, ...prev])} />
        <TagFilter entries={entries} onTagSelect={setActiveTag} activeTag={activeTag} />
        <EntryGrid entries={filterEntries(entries, activeTag)} />
      </main>
    </div>
  )
}
