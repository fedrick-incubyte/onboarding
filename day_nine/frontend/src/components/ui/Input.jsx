const inputCls = 'w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-brand-500 transition-colors'

export function Input({ id, type = 'text', onChange, value, placeholder, error }) {
  const handler = onChange ? e => onChange(e.target.value) : undefined
  const cls = `${inputCls}${error ? ' border-red-500' : ''}`
  if (type === 'textarea') return <textarea id={id} className={cls} onChange={handler} value={value} placeholder={placeholder} />
  return (
    <>
      <input id={id} type={type} className={cls} onChange={handler} value={value} placeholder={placeholder} />
      {error && <p>{error}</p>}
    </>
  )
}
