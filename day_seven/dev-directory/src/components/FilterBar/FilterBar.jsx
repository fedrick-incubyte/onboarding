import { useSkillFilter } from '../../hooks/useSkillFilter';

export function FilterBar({ skills, onFilterChange }) {
  const { activeSkill, selectSkill, clearFilter } = useSkillFilter();

  function handleSkillClick(skill) {
    selectSkill(skill);
    onFilterChange(activeSkill === skill ? null : skill);
  }

  function handleClearFilter() {
    clearFilter();
    onFilterChange(null);
  }

  return (
    <div>
      <button onClick={handleClearFilter}>All</button>
      {skills.map((skill) => (
        <button
          key={skill}
          onClick={() => handleSkillClick(skill)}
          aria-pressed={activeSkill === skill}
        >
          {skill}
        </button>
      ))}
    </div>
  );
}
