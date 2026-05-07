import { Badge } from './ui/Badge.jsx'
import { getAllTags } from '../domain/tag.js'

export function TagFilter({ entries }) {
  const tags = getAllTags(entries)
  return (
    <div>
      <Badge label="All" />
      {tags.map(tag => <Badge key={tag} label={tag} />)}
    </div>
  )
}
