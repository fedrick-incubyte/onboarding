import { useEffect, useState } from 'react'
import { getTasks } from '../api/taskService'

export function useTasks() {
  const [tasks, setTasks] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    getTasks().then(setTasks).catch(setError).finally(() => setIsLoading(false))
  }, [])

  function addTask(task) { setTasks(prev => [...prev, task]) }
  function removeTask(id) { setTasks(prev => prev.filter(t => t.id !== id)) }

  return { tasks, isLoading, error, addTask, removeTask }
}
