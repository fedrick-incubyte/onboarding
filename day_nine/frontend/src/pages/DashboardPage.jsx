import { useTasks } from '../hooks/useTasks'

export default function DashboardPage() {
  const { tasks, isLoading } = useTasks()
  if (isLoading) return <p>Loading...</p>
  return (
    <div>
      <ul>
        {tasks.map(t => <li key={t.id}>{t.title}</li>)}
      </ul>
    </div>
  )
}
