import { render, screen, fireEvent } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { DeveloperDirectory } from './DeveloperDirectory';

const renderWithRouter = (ui) => render(<MemoryRouter>{ui}</MemoryRouter>);

describe('DeveloperDirectory', () => {
  it('should render all developers on initial load', () => {
    renderWithRouter(<DeveloperDirectory />);
    expect(screen.getByText('Ada Lovelace')).toBeInTheDocument();
    expect(screen.getByText('Grace Hopper')).toBeInTheDocument();
    expect(screen.getByText('Linus Torvalds')).toBeInTheDocument();
    expect(screen.getByText('Margaret Hamilton')).toBeInTheDocument();
  });

  it('should filter developers when a skill is selected', () => {
    renderWithRouter(<DeveloperDirectory />);
    fireEvent.click(screen.getByRole('button', { name: 'Node.js' }));
    expect(screen.getByText('Grace Hopper')).toBeInTheDocument();
    expect(screen.getByText('Linus Torvalds')).toBeInTheDocument();
    expect(screen.queryByText('Ada Lovelace')).not.toBeInTheDocument();
    expect(screen.queryByText('Margaret Hamilton')).not.toBeInTheDocument();
  });

  it('should show all developers when the filter is cleared', () => {
    renderWithRouter(<DeveloperDirectory />);
    fireEvent.click(screen.getByRole('button', { name: 'Node.js' }));
    fireEvent.click(screen.getByRole('button', { name: 'All' }));
    expect(screen.getByText('Ada Lovelace')).toBeInTheDocument();
    expect(screen.getByText('Grace Hopper')).toBeInTheDocument();
    expect(screen.getByText('Linus Torvalds')).toBeInTheDocument();
    expect(screen.getByText('Margaret Hamilton')).toBeInTheDocument();
  });
});
