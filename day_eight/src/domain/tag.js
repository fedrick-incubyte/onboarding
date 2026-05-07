export function parseTag(raw) {
  if (!raw.trim()) return null
  return raw.trim().toLowerCase()
}

export function getAllTags(entries) {
  return [...new Set(entries.flatMap(e => e.tags))]
}
