import { render, screen } from '@testing-library/react';
import { Home } from './Home';

describe('Home', () => {
  it('should render without crashing', () => {
    render(<Home />);
    expect(document.body).toBeInTheDocument();
  });
});
