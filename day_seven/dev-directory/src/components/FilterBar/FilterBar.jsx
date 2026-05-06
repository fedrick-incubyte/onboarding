export function FilterBar({ skills, onFilterChange }) {
  return (
    <div>
      {skills.map((skill) => (
        <button key={skill}>{skill}</button>
      ))}
    </div>
  );
}
