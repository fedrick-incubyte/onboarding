import { useState } from 'react';

export function FilterBar({ skills, onFilterChange }) {
  const [activeSkill, setActiveSkill] = useState(null);

  function handleSkillClick(skill) {
    const nextSkill = activeSkill === skill ? null : skill;
    setActiveSkill(nextSkill);
    onFilterChange(nextSkill);
  }

  return (
    <div>
      <button>All</button>
      {skills.map((skill) => (
        <button key={skill} onClick={() => handleSkillClick(skill)}>{skill}</button>
      ))}
    </div>
  );
}
