export function Card({ children }) {
  return (
    <div className="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-5 shadow-sm hover:shadow-md transition-shadow">
      {children}
    </div>
  )
}

Card.Header = function CardHeader({ children }) {
  return (
    <div className="mb-3 pb-3 border-b border-slate-100 dark:border-slate-700">
      {children}
    </div>
  )
}
