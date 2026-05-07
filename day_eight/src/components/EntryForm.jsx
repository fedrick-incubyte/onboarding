import { useState } from 'react'
import { createEntry } from '../domain/entry.js'
import { parseTag } from '../domain/tag.js'

export function EntryForm({ onSubmit }) {
  const [title, setTitle] = useState('')
  const [body, setBody] = useState('')
  const [tagsInput, setTagsInput] = useState('')

  function handleSubmit() {
    const tags = tagsInput.split(',').map(parseTag).filter(Boolean)
    onSubmit(createEntry(title, body, tags))
    setTitle('')
    setBody('')
    setTagsInput('')
  }

  return (
    <>
      <input placeholder="Title" value={title} onChange={e => setTitle(e.target.value)} />
      <input placeholder="Body" value={body} onChange={e => setBody(e.target.value)} />
      <input placeholder="Tags" value={tagsInput} onChange={e => setTagsInput(e.target.value)} />
      <button onClick={handleSubmit}>Add</button>
    </>
  )
}
