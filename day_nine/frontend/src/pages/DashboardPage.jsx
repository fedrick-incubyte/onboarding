import { useContext } from 'react'
import { useTasks } from '../hooks/useTasks'
import { TaskCard } from '../components/TaskCard'
import { TaskForm } from '../components/TaskForm'
import { createTask } from '../api/taskService'
import { AuthContext } from '../context/AuthContext'

export default function DashboardPage() {
  const { logout } = useContext(AuthContext)
  const { tasks, isLoading, error, addTask, removeTask } = useTasks()
  if (isLoading) return (
    <div className="min-h-screen flex items-center justify-center">
      <p className="text-gray-400 text-sm">Loading…</p>
    </div>
  )
  if (error) return (
    <div className="min-h-screen flex items-center justify-center">
      <p className="text-red-500 text-sm">Failed to load tasks</p>
    </div>
  )

  async function handleAdd(title) {
    const task = await createTask({ title })
    addTask(task)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white border-b border-gray-200 px-6 py-4 flex items-center justify-between">
        <h1 className="text-lg font-semibold text-gray-900">My Tasks</h1>
        <button
          onClick={logout}
          className="text-sm text-gray-500 hover:text-gray-800 transition-colors"
        >
          Logout
        </button>
      </header>
      <main className="max-w-2xl mx-auto px-4 py-8 space-y-6">
        <TaskForm onAdd={handleAdd} />
        {tasks.length === 0
          ? <p className="text-center text-sm text-gray-400 py-12">No tasks yet — add one above</p>
          : <ul className="space-y-3">{tasks.map(t => <TaskCard key={t.id} task={t} onDelete={removeTask} />)}</ul>
        }
      </main>
    </div>
  )
}
