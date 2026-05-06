import { render, screen, fireEvent } from '@testing-library/react';
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

  it('should call onFilterChange with the skill name when a skill button is clicked', () => {
    const handleFilterChange = vi.fn();
    render(<FilterBar skills={skills} onFilterChange={handleFilterChange} />);
    fireEvent.click(screen.getByRole('button', { name: 'React' }));
    expect(handleFilterChange).toHaveBeenCalledWith('React');
  });

  it('should call onFilterChange with null when the active skill is clicked again', () => {
    const handleFilterChange = vi.fn();
    render(<FilterBar skills={skills} onFilterChange={handleFilterChange} />);
    fireEvent.click(screen.getByRole('button', { name: 'React' }));
    fireEvent.click(screen.getByRole('button', { name: 'React' }));
    expect(handleFilterChange).toHaveBeenLastCalledWith(null);
  });
});
