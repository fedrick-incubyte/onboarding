import { useState } from 'react'
import { createEntry } from '../domain/entry.js'

export function EntryForm({ onSubmit }) {
  const [title, setTitle] = useState('')
  const [body, setBody] = useState('')

  function handleSubmit() {
    onSubmit(createEntry(title, body, []))
  }

  return (
    <>
      <input placeholder="Title" value={title} onChange={e => setTitle(e.target.value)} />
      <input placeholder="Body" value={body} onChange={e => setBody(e.target.value)} />
      <button onClick={handleSubmit}>Add</button>
    </>
  )
}
