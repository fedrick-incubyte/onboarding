export function Input({ type = 'text', onChange }) {
  const handler = e => onChange(e.target.value)
  if (type === 'textarea') return <textarea onChange={handler} />
  return <input type="text" onChange={handler} />
}
