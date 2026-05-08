export function Button({ children, onClick, disabled, variant }) {
  const base = 'px-5 py-2 font-medium rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-brand-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed'
  const cls = variant === 'secondary'
    ? `${base} bg-white border border-brand-500 text-brand-500 hover:bg-brand-50`
    : `${base} bg-brand-500 text-white hover:bg-brand-900`
  return <button className={cls} onClick={onClick} disabled={disabled}>{children}</button>
}
