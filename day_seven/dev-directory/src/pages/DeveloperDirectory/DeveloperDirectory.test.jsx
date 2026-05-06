import { render, screen } from '@testing-library/react';
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
});
