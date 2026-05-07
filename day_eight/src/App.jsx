import { useState } from 'react'
import { EntryForm } from './components/EntryForm.jsx'
import { EntryGrid } from './components/EntryGrid.jsx'
import { TagFilter } from './components/TagFilter.jsx'
import { filterEntries } from './domain/filter.js'

export default function App() {
  const [entries, setEntries] = useState([])
  const [activeTag, setActiveTag] = useState(null)

  return (
    <div>
      <EntryForm onSubmit={entry => setEntries(prev => [entry, ...prev])} />
      <TagFilter entries={entries} onTagSelect={setActiveTag} />
      <EntryGrid entries={filterEntries(entries, activeTag)} />
    </div>
  )
}
