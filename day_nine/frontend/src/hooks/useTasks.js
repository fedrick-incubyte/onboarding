import { useState } from 'react'

export function useTasks() {
  const [tasks, setTasks] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState(null)

  return { tasks, isLoading, error }
}
