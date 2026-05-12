import { useTasks } from '../hooks/useTasks'
import { TaskCard } from '../components/TaskCard'
import { TaskForm } from '../components/TaskForm'
import { createTask } from '../api/taskService'

export default function DashboardPage() {
  const { tasks, isLoading, error, addTask, removeTask } = useTasks()
  if (isLoading) return <p>Loading...</p>
  if (error) return <p>Failed to load tasks</p>

  async function handleAdd(title) {
    const task = await createTask({ title })
    addTask(task)
  }

  return (
    <div>
      <TaskForm onAdd={handleAdd} />
      <ul>
        {tasks.map(t => <TaskCard key={t.id} task={t} onDelete={removeTask} />)}
      </ul>
    </div>
  )
}
