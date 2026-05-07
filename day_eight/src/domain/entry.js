export function createEntry(title, body, tags) {
  if (!title.trim()) throw new Error('Title is required')
  return { id: crypto.randomUUID(), title, body, tags, createdAt: new Date().toISOString() }
}
