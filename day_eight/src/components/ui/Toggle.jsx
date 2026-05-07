export function Toggle({ onToggle, checked }) {
  return <button role="switch" aria-checked={checked} onClick={onToggle} />
}
