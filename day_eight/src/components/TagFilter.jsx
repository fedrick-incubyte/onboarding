import { Badge } from './ui/Badge.jsx'
import { getAllTags } from '../domain/tag.js'

export function TagFilter({ entries, onTagSelect }) {
  const tags = getAllTags(entries)
  return (
    <div>
      <Badge label="All" clickable onClick={() => onTagSelect(null)} />
      {tags.map(tag => <Badge key={tag} label={tag} clickable onClick={() => onTagSelect(tag)} />)}
    </div>
  )
}
