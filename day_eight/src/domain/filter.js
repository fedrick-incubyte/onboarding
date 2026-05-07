export function filterEntries(entries, tag) {
  if (!tag) return entries
  return entries.filter(e => e.tags.includes(tag))
}
