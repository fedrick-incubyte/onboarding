import { Link } from 'react-router-dom';
import { Badge } from '../Badge/Badge';

export function DeveloperCard({ developer }) {
  return (
    <article>
      <Link to={`/developers/${developer.id}`}>
        <img src={developer.avatar} alt={developer.name} />
        <p>{developer.name}</p>
      </Link>
      <p>{developer.role}</p>
      <p>{developer.location}</p>
      <ul>
        {developer.skills.map((skill) => (
          <li key={skill}>
            <Badge label={skill} />
          </li>
        ))}
      </ul>
    </article>
  );
}
