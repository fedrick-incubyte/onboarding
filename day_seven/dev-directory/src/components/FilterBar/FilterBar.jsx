import { useState } from 'react';

export function FilterBar({ skills, onFilterChange }) {
  const [activeSkill, setActiveSkill] = useState(null);

  function handleSkillClick(skill) {
    const nextSkill = activeSkill === skill ? null : skill;
    setActiveSkill(nextSkill);
    onFilterChange(nextSkill);
  }

  function handleClearFilter() {
    setActiveSkill(null);
    onFilterChange(null);
  }

  return (
    <div>
      <button onClick={handleClearFilter}>All</button>
      {skills.map((skill) => (
        <button key={skill} onClick={() => handleSkillClick(skill)}>{skill}</button>
      ))}
    </div>
  );
}
