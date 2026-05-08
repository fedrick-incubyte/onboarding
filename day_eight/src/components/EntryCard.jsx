import { Badge } from './ui/Badge.jsx'
import { Card } from './ui/Card.jsx'

export function EntryCard({ entry }) {
  return (
    <Card>
      <p className="font-semibold text-slate-900 dark:text-slate-100">{entry.title}</p>
      {entry.tags.length > 0 && (
        <div className="flex flex-wrap gap-1 mt-3">
          {entry.tags.map(tag => <Badge key={tag} label={tag} />)}
        </div>
      )}
    </Card>
  )
}
