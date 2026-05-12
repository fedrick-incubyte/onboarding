import { useContext } from 'react'
import { useTasks } from '../hooks/useTasks'
import { TaskCard } from '../components/TaskCard'
import { TaskForm } from '../components/TaskForm'
import { createTask } from '../api/taskService'
import { AuthContext } from '../context/AuthContext'

export default function DashboardPage() {
  const { logout } = useContext(AuthContext)
  const { tasks, isLoading, error, addTask, removeTask } = useTasks()
  if (isLoading) return <p>Loading...</p>
  if (error) return <p>Failed to load tasks</p>

  async function handleAdd(title) {
    const task = await createTask({ title })
    addTask(task)
  }

  return (
    <div>
      <button onClick={logout}>Logout</button>
      <TaskForm onAdd={handleAdd} />
      <ul>
        {tasks.map(t => <TaskCard key={t.id} task={t} onDelete={removeTask} />)}
      </ul>
    </div>
  )
}
