import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import App from './App';

describe('App', () => {
  it('should render the navigation', () => {
    render(<MemoryRouter><App /></MemoryRouter>);
    expect(screen.getByRole('navigation')).toBeInTheDocument();
  });
});
