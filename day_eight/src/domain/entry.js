export function createEntry(title, body, tags) {
  return { id: '1', title, body, tags, createdAt: new Date().toISOString() }
}
