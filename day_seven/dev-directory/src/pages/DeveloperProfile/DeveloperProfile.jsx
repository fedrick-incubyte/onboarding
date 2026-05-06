import { useParams, Link } from 'react-router-dom';
import { developers } from '../../data/developers';
import { Badge } from '../../components/Badge/Badge';

export function DeveloperProfile() {
  const { id } = useParams();
  const developer = developers.find((d) => d.id === id);

  if (!developer) return <p>Developer not found</p>;

  return (
    <div>
      <h1>{developer.name}</h1>
      <p>{developer.bio}</p>
      <ul>
        {developer.skills.map((skill) => (
          <li key={skill}><Badge label={skill} /></li>
        ))}
      </ul>
      <Link to="/developers">Back to Directory</Link>
    </div>
  );
}
