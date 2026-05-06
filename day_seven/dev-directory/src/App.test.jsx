import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import App from './App';

describe('App', () => {
  it('should render the navigation', () => {
    render(<MemoryRouter><App /></MemoryRouter>);
    expect(screen.getByRole('navigation')).toBeInTheDocument();
  });

  it('should render the Home page at /', () => {
    render(
      <MemoryRouter initialEntries={['/']}>
        <App />
      </MemoryRouter>
    );
    expect(screen.getByRole('heading', { name: /devdirectory/i })).toBeInTheDocument();
  });
});
