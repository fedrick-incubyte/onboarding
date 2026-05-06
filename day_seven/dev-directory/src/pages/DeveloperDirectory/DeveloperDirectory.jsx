import { useState, useEffect } from 'react';
import { developers as allDevelopers } from '../../data/developers';
import { DeveloperCard } from '../../components/DeveloperCard/DeveloperCard';
import { FilterBar } from '../../components/FilterBar/FilterBar';
import styles from './DeveloperDirectory.module.css';

export function DeveloperDirectory() {
  const [developers, setDevelopers] = useState([]);
  const [activeFilter, setActiveFilter] = useState(null);

  useEffect(() => {
    setDevelopers(allDevelopers);
  }, []);

  const visibleDevelopers = activeFilter
    ? developers.filter((d) => d.skills.includes(activeFilter))
    : developers;

  const uniqueSkills = [...new Set(allDevelopers.flatMap((d) => d.skills))];

  function handleFilterChange(skill) {
    setActiveFilter(skill);
  }

  return (
    <div className={styles.wrapper}>
      <FilterBar skills={uniqueSkills} onFilterChange={handleFilterChange} />
      {visibleDevelopers.length === 0
        ? <p className={styles.empty}>No developers found</p>
        : (
          <div className={styles.grid}>
            {visibleDevelopers.map((developer) => (
              <DeveloperCard key={developer.id} developer={developer} />
            ))}
          </div>
        )
      }
    </div>
  );
}
