export function validateTask({ title }) {
  if (!title) throw new Error('Title is required')
}
