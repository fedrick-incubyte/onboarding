import { NavLink } from 'react-router-dom';
import { ThemeToggle } from '../ThemeToggle/ThemeToggle';
import styles from './Navigation.module.css';

export function Navigation() {
  return (
    <nav className={styles.nav}>
      <span className={styles.brand}>DevDirectory</span>
      <div className={styles.links}>
        <NavLink
          to="/"
          className={({ isActive }) =>
            isActive ? `${styles.link} ${styles.activeLink} active` : styles.link
          }
        >
          Home
        </NavLink>
        <NavLink
          to="/developers"
          className={({ isActive }) =>
            isActive ? `${styles.link} ${styles.activeLink} active` : styles.link
          }
        >
          Developers
        </NavLink>
        <NavLink
          to="/about"
          className={({ isActive }) =>
            isActive ? `${styles.link} ${styles.activeLink} active` : styles.link
          }
        >
          About
        </NavLink>
      </div>
      <div className={styles.actions}>
        <ThemeToggle />
      </div>
    </nav>
  );
}
