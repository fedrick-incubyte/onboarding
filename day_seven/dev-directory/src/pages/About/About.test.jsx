import { render, screen } from '@testing-library/react';
import { About } from './About';

describe('About', () => {
  it('should render without crashing', () => {
    render(<About />);
    expect(document.body).toBeInTheDocument();
  });
});
