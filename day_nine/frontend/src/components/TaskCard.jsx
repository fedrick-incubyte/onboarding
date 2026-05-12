import { Badge } from './ui/Badge'
import { TASK_STATUS } from '../domain/task'

const STATUS_VARIANT = {
  [TASK_STATUS.DONE]: 'status-done',
  [TASK_STATUS.IN_PROGRESS]: 'status-in_progress',
}

export function TaskCard({ task, onDelete }) {
  return (
    <li>
      {task.title}
      <Badge label={task.status} variant={STATUS_VARIANT[task.status]} />
      <button onClick={() => onDelete(task.id)}>Delete</button>
    </li>
  )
}
