import { useState } from 'react'

export function TaskForm({ onAdd }) {
  const [title, setTitle] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    if (!title.trim()) return
    await onAdd(title.trim())
    setTitle('')
  }

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="New task" value={title} onChange={e => setTitle(e.target.value)} />
      <button type="submit">Add</button>
    </form>
  )
}
