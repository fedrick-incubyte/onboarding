import { useState } from 'react'
import { createEntry } from '../domain/entry.js'
import { parseTag } from '../domain/tag.js'
import { Input } from './ui/Input.jsx'
import { Button } from './ui/Button.jsx'

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
    <div className="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-6 shadow-sm space-y-4">
      <h2 className="text-lg font-semibold text-slate-700 dark:text-slate-300">New Entry</h2>
      <Input placeholder="Title" value={title} onChange={setTitle} />
      <Input placeholder="Body" value={body} onChange={setBody} />
      <Input placeholder="Tags" value={tagsInput} onChange={setTagsInput} />
      <Button onClick={handleSubmit}>Add</Button>
    </div>
  )
}
