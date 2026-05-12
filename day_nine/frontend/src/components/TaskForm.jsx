import { useState } from 'react'
import { Input } from './ui/Input'
import { Button } from './ui/Button'

export function TaskForm({ onAdd }) {
  const [title, setTitle] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    if (!title.trim()) return
    await onAdd(title.trim())
    setTitle('')
  }

  return (
    <form onSubmit={handleSubmit} className="flex gap-2">
      <div className="flex-1">
        <Input value={title} onChange={setTitle} placeholder="New task" />
      </div>
      <Button type="submit">Add</Button>
    </form>
  )
}
