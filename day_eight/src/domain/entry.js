export function createEntry(title, body, tags) {
  if (!title.trim()) throw new Error('Title is required')
  if (title.length > 100) throw new Error('Title too long')
  return { id: crypto.randomUUID(), title, body, tags, createdAt: new Date().toISOString() }
}
