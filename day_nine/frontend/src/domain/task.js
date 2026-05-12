export function validateTask({ title }) {
  if (!title) throw new Error('Title is required')
  if (title.length > 200) throw new Error('Title too long')
}

export function normalizeTask({ title, ...rest }) {
  return { title: title.trim(), ...rest }
}
