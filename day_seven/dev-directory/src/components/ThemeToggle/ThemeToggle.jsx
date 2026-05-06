import { useTheme } from '../../context/ThemeContext';
import styles from './ThemeToggle.module.css';

export function ThemeToggle() {
  const { toggleTheme } = useTheme();
  return (
    <div className={styles.wrapper}>
      <button className={styles.button} onClick={toggleTheme}>Toggle theme</button>
    </div>
  );
}
