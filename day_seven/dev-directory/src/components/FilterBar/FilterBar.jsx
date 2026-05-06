export function FilterBar({ skills, onFilterChange }) {
  return (
    <div>
      <button>All</button>
      {skills.map((skill) => (
        <button key={skill} onClick={() => onFilterChange(skill)}>{skill}</button>
      ))}
    </div>
  );
}
