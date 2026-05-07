export function Button({ children, onClick, disabled, variant }) {
  const cls = variant === 'secondary' ? 'bg-white border border-brand-500 text-brand-500' : 'bg-brand-500 text-white'
  return <button className={cls} onClick={onClick} disabled={disabled}>{children}</button>
}
