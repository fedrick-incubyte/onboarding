import { NavLink } from 'react-router-dom';
import { ThemeToggle } from '../ThemeToggle/ThemeToggle';

export function Navigation() {
  return (
    <nav>
      <NavLink to="/">Home</NavLink>
      <NavLink to="/developers">Developers</NavLink>
      <NavLink to="/about">About</NavLink>
      <ThemeToggle />
    </nav>
  );
}
