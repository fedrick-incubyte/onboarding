import { useState } from 'react'
import { EntryForm } from './components/EntryForm.jsx'
import { EntryGrid } from './components/EntryGrid.jsx'

export default function App() {
  const [entries, setEntries] = useState([])

  return (
    <div>
      <EntryForm onSubmit={entry => setEntries(prev => [entry, ...prev])} />
      <EntryGrid entries={entries} />
    </div>
  )
}
