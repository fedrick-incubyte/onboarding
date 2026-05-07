export function parseTag(raw) {
  if (!raw.trim()) return null
  return raw.trim().toLowerCase()
}
