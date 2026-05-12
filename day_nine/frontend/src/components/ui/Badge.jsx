const STATUS_COLORS = {
  'status-done': 'bg-green-100 text-green-800',
  'status-in_progress': 'bg-yellow-100 text-yellow-800',
}

export function Badge({ label, clickable, onClick, active, variant }) {
  const base = 'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium transition-colors'
  let style
  if (variant && STATUS_COLORS[variant]) {
    style = `${base} ${STATUS_COLORS[variant]}`
  } else if (clickable) {
    style = active
      ? `${base} bg-brand-500 text-white cursor-pointer`
      : `${base} bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 hover:bg-brand-500 hover:text-white cursor-pointer`
  } else {
    style = `${base} bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300`
  }
  return <span className={style} onClick={clickable ? onClick : undefined}>{label}</span>
}
