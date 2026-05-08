import { EntryCard } from './EntryCard.jsx'

export function EntryGrid({ entries }) {
  if (!entries.length) return (
    <p className="text-center text-slate-400 dark:text-slate-500 py-16 text-lg">No entries yet.</p>
  )
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 lg:gap-6">
      {entries.map(e => <EntryCard key={e.id} entry={e} />)}
    </div>
  )
}
