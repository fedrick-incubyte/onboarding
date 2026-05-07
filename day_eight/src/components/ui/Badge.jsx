export function Badge({ label, clickable, onClick }) {
  return <span onClick={clickable ? onClick : undefined}>{label}</span>
}
