import { useTasks } from '../hooks/useTasks'

export default function DashboardPage() {
  const { isLoading } = useTasks()
  if (isLoading) return <p>Loading...</p>
  return <div>Dashboard</div>
}
