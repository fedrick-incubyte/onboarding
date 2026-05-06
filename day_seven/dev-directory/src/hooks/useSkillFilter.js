import { useState } from 'react';

export function useSkillFilter() {
  const [activeSkill, setActiveSkill] = useState(null);

  function selectSkill(skill) {
    const nextSkill = activeSkill === skill ? null : skill;
    setActiveSkill(nextSkill);
  }

  function clearFilter() {
    setActiveSkill(null);
  }

  return { activeSkill, selectSkill, clearFilter };
}
