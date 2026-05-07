function validateEntry(title, body) {
  if (!title.trim()) throw new Error('Title is required')
  if (title.length > 100) throw new Error('Title too long')
  if (!body.trim()) throw new Error('Body is required')
}

export function createEntry(title, body, tags) {
  validateEntry(title, body)
  return { id: crypto.randomUUID(), title, body, tags, createdAt: new Date().toISOString() }
}
