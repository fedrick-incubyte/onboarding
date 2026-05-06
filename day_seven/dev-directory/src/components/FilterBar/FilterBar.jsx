import { useSkillFilter } from '../../hooks/useSkillFilter';
import styles from './FilterBar.module.css';

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
    <div className={styles.wrapper}>
      <button className={styles.button} onClick={handleClearFilter}>All</button>
      {skills.map((skill) => (
        <button
          key={skill}
          className={styles.button}
          onClick={() => handleSkillClick(skill)}
          aria-pressed={activeSkill === skill}
        >
          {skill}
        </button>
      ))}
    </div>
  );
}
