import { render, screen } from '@testing-library/react';
import { Badge } from './Badge';

describe('Badge', () => {
  test('renders the label text', () => {
    render(<Badge label="React" />);
    expect(screen.getByText('React')).toBeInTheDocument();
  });
});