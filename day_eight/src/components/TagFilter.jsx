import { Badge } from './ui/Badge.jsx'
import { getAllTags } from '../domain/tag.js'

export function TagFilter({ entries, onTagSelect, activeTag }) {
  const tags = getAllTags(entries)
  return (
    <div className="flex flex-wrap gap-2">
      <Badge label="All" clickable onClick={() => onTagSelect(null)} active={activeTag === null} />
      {tags.map(tag => (
        <Badge key={tag} label={tag} clickable onClick={() => onTagSelect(tag)} active={activeTag === tag} />
      ))}
    </div>
  )
}
