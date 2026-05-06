import styles from './Badge.module.css';

export function Badge({ label }) {
  return <span className={styles.badge}>{label}</span>;
}