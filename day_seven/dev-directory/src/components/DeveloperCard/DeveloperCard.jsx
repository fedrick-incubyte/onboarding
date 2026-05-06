import { Badge } from '../Badge/Badge';

export function DeveloperCard({ developer }) {
  return (
    <article>
      <img src={developer.avatar} alt={developer.name} />
      <p>{developer.name}</p>
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
