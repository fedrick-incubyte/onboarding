import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { Navigation } from './Navigation';

const renderWithRouter = (ui) => render(<MemoryRouter>{ui}</MemoryRouter>);

describe('Navigation', () => {
  it('should render a link to the home page', () => {
    renderWithRouter(<Navigation />);
    expect(screen.getByRole('link', { name: /home/i })).toBeInTheDocument();
  });

  it('should render a link to the developers page', () => {
    renderWithRouter(<Navigation />);
    expect(screen.getByRole('link', { name: /developers/i })).toBeInTheDocument();
  });

  it('should render a link to the about page', () => {
    renderWithRouter(<Navigation />);
    expect(screen.getByRole('link', { name: /about/i })).toBeInTheDocument();
  });

  it('should apply an active class to the current route link', () => {
    render(
      <MemoryRouter initialEntries={['/developers']}>
        <Navigation />
      </MemoryRouter>
    );
    expect(screen.getByRole('link', { name: /developers/i })).toHaveClass('active');
  });
});
