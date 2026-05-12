import { useTasks } from '../hooks/useTasks'

export default function DashboardPage() {
  const { tasks, isLoading, error } = useTasks()
  if (isLoading) return <p>Loading...</p>
  if (error) return <p>Failed to load tasks</p>
  return (
    <div>
      <ul>
        {tasks.map(t => <li key={t.id}>{t.title}</li>)}
      </ul>
    </div>
  )
}
