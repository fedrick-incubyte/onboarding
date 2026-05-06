import { NavLink } from 'react-router-dom';

export function Navigation() {
  return (
    <nav>
      <NavLink to="/">Home</NavLink>
      <NavLink to="/developers">Developers</NavLink>
      <NavLink to="/about">About</NavLink>
    </nav>
  );
}
