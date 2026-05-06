import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { ThemeProvider } from '../../context/ThemeContext';
import { Navigation } from './Navigation';

const renderWithProviders = (ui) =>
  render(
    <ThemeProvider>
      <MemoryRouter>{ui}</MemoryRouter>
    </ThemeProvider>
  );

describe('Navigation', () => {
  it('should render a link to the home page', () => {
    renderWithProviders(<Navigation />);
    expect(screen.getByRole('link', { name: /home/i })).toBeInTheDocument();
  });

  it('should render a link to the developers page', () => {
    renderWithProviders(<Navigation />);
    expect(screen.getByRole('link', { name: /developers/i })).toBeInTheDocument();
  });

  it('should render a link to the about page', () => {
    renderWithProviders(<Navigation />);
    expect(screen.getByRole('link', { name: /about/i })).toBeInTheDocument();
  });

  it('should apply an active class to the current route link', () => {
    render(
      <ThemeProvider>
        <MemoryRouter initialEntries={['/developers']}>
          <Navigation />
        </MemoryRouter>
      </ThemeProvider>
    );
    expect(screen.getByRole('link', { name: /developers/i })).toHaveClass('active');
  });

  it('should render a theme toggle button', () => {
    renderWithProviders(<Navigation />);
    expect(screen.getByRole('button', { name: /toggle theme/i })).toBeInTheDocument();
  });
});
