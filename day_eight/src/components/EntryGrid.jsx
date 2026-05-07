import { EntryCard } from './EntryCard.jsx'

export function EntryGrid({ entries }) {
  return <div>{entries.map(e => <EntryCard key={e.id} entry={e} />)}</div>
}
