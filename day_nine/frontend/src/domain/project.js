export function validateProject({ name }) {
  if (!name) throw new Error('Name is required')
}
