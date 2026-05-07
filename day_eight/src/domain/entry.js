export function createEntry(title, body, tags) {
  return { id: crypto.randomUUID(), title, body, tags, createdAt: new Date().toISOString() }
}
