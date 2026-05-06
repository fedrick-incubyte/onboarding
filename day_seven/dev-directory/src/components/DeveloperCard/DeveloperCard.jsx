import { Link } from 'react-router-dom';
import { Badge } from '../Badge/Badge';
import styles from './DeveloperCard.module.css';

export function DeveloperCard({ developer }) {
  return (
    <article className={styles.card}>
      <img className={styles.avatar} src={developer.avatar} alt={developer.name} />
      <div className={styles.body}>
        <p className={styles.name}>
          <Link to={`/developers/${developer.id}`}>{developer.name}</Link>
        </p>
        <p className={styles.role}>{developer.role}</p>
        <p className={styles.location}>{developer.location}</p>
        <ul className={styles.skills}>
          {developer.skills.map((skill) => (
            <li key={skill}>
              <Badge label={skill} />
            </li>
          ))}
        </ul>
      </div>
    </article>
  );
}
