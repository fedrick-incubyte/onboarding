import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import App from './App';

const renderApp = (initialEntries = ['/']) =>
  render(
    <ThemeProvider>
      <MemoryRouter initialEntries={initialEntries}>
        <App />
      </MemoryRouter>
    </ThemeProvider>
  );

describe('App', () => {
  it('should render the navigation', () => {
    renderApp();
    expect(screen.getByRole('navigation')).toBeInTheDocument();
  });

  it('should render the Home page at /', () => {
    renderApp(['/']);
    expect(screen.getByRole('heading', { name: /devdirectory/i })).toBeInTheDocument();
  });
});
