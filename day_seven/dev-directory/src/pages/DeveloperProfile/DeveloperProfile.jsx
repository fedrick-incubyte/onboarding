import { useParams } from 'react-router-dom';
import { developers } from '../../data/developers';
import { Badge } from '../../components/Badge/Badge';

export function DeveloperProfile() {
  const { id } = useParams();
  const developer = developers.find((d) => d.id === id);

  return (
    <div>
      <h1>{developer.name}</h1>
      <p>{developer.bio}</p>
      <ul>
        {developer.skills.map((skill) => (
          <li key={skill}><Badge label={skill} /></li>
        ))}
      </ul>
    </div>
  );
}
