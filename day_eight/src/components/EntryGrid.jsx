import { EntryCard } from './EntryCard.jsx'

export function EntryGrid({ entries }) {
  if (!entries.length) return <p>No entries yet.</p>
  return <div>{entries.map(e => <EntryCard key={e.id} entry={e} />)}</div>
}
