import { useTasks } from '../hooks/useTasks'
import { TaskCard } from '../components/TaskCard'

export default function DashboardPage() {
  const { tasks, isLoading, error, removeTask } = useTasks()
  if (isLoading) return <p>Loading...</p>
  if (error) return <p>Failed to load tasks</p>
  return (
    <div>
      <ul>
        {tasks.map(t => <TaskCard key={t.id} task={t} onDelete={removeTask} />)}
      </ul>
    </div>
  )
}
