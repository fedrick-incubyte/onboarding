export function Input({ type = 'text' }) {
  if (type === 'textarea') return <textarea />
  return <input type="text" />
}
