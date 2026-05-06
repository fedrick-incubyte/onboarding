import { useState, useEffect } from 'react';
import { developers as allDevelopers } from '../../data/developers';
import { DeveloperCard } from '../../components/DeveloperCard/DeveloperCard';

export function DeveloperDirectory() {
  const [developers, setDevelopers] = useState([]);

  useEffect(() => {
    setDevelopers(allDevelopers);
  }, []);

  return (
    <div>
      {developers.map((developer) => (
        <DeveloperCard key={developer.id} developer={developer} />
      ))}
    </div>
  );
}
