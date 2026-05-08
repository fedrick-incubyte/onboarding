export function Badge({ label, clickable, onClick, active }) {
  const base = 'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium transition-colors'
  const style = clickable
    ? active
      ? `${base} bg-brand-500 text-white cursor-pointer`
      : `${base} bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 hover:bg-brand-500 hover:text-white cursor-pointer`
    : `${base} bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300`
  return <span className={style} onClick={clickable ? onClick : undefined}>{label}</span>
}
