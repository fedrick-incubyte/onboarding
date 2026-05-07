import { Badge } from './ui/Badge.jsx'

export function EntryCard({ entry }) {
  return (
    <div>
      <div>{entry.title}</div>
      <div>{entry.tags.map(tag => <Badge key={tag} label={tag} />)}</div>
    </div>
  )
}
