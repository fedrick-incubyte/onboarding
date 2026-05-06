import { useParams, Link } from 'react-router-dom';
import { developers } from '../../data/developers';
import { Badge } from '../../components/Badge/Badge';
import styles from './DeveloperProfile.module.css';

export function DeveloperProfile() {
  const { id } = useParams();
  const developer = developers.find((d) => d.id === id);

  if (!developer) return <p>Developer not found</p>;

  return (
    <div className={styles.wrapper}>
      <img src={developer.avatar} alt={developer.name} className={styles.avatar} />
      <h1>{developer.name}</h1>
      <p className={styles.bio}>{developer.bio}</p>
      <ul className={styles.skills}>
        {developer.skills.map((skill) => (
          <li key={skill}><Badge label={skill} /></li>
        ))}
      </ul>
      <Link to="/developers" className={styles.backLink}>Back to Directory</Link>
    </div>
  );
}
