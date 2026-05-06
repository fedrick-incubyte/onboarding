import { render, screen } from '@testing-library/react';
import { FilterBar } from './FilterBar';

const skills = ['React', 'Node.js', 'CSS'];

describe('FilterBar', () => {
  it('should render a button for each skill', () => {
    render(<FilterBar skills={skills} onFilterChange={() => {}} />);
    expect(screen.getByRole('button', { name: 'React' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Node.js' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'CSS' })).toBeInTheDocument();
  });

  it('should render an All button', () => {
    render(<FilterBar skills={skills} onFilterChange={() => {}} />);
    expect(screen.getByRole('button', { name: 'All' })).toBeInTheDocument();
  });
});
