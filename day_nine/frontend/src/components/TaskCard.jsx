import { Badge } from './ui/Badge'
import { TASK_STATUS } from '../domain/task'

const STATUS_VARIANT = {
  [TASK_STATUS.DONE]: 'status-done',
  [TASK_STATUS.IN_PROGRESS]: 'status-in_progress',
}

export function TaskCard({ task, onDelete }) {
  return (
    <li className="flex items-center justify-between bg-white border border-gray-200 rounded-xl px-4 py-3 shadow-sm">
      <div className="flex items-center gap-3 min-w-0">
        <span className="text-sm text-gray-800 truncate">{task.title}</span>
        <Badge label={task.status} variant={STATUS_VARIANT[task.status]} />
      </div>
      <button
        onClick={() => onDelete(task.id)}
        className="ml-4 text-xs text-gray-400 hover:text-red-500 transition-colors shrink-0"
      >
        Delete
      </button>
    </li>
  )
}
