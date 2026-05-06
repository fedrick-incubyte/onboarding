import { render, screen } from '@testing-library/react';
import { Home } from './Home';

describe('Home', () => {
  it('should render a welcome heading', () => {
    render(<Home />);
    expect(screen.getByRole('heading', { name: /devdirectory/i })).toBeInTheDocument();
  });
});
