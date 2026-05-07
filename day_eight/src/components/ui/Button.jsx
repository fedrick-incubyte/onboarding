export function Button({ children, onClick, disabled }) {
  return <button className="bg-brand-500 text-white" onClick={onClick} disabled={disabled}>{children}</button>
}
