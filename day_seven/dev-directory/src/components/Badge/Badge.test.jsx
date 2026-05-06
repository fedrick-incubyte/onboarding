import { render, screen } from '@testing-library/react';
import { Badge } from './Badge';

describe('Badge', () => {
  it('should render the label text', () => {
    render(<Badge label="React" />);
    expect(screen.getByText('React')).toBeInTheDocument();
  });

  it('should render without crashing when label is an empty string', () => {
    const { container } = render(<Badge label="" />);
    expect(container.firstChild).toBeInTheDocument();
  });
});