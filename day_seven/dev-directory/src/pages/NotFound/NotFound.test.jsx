import { render, screen } from '@testing-library/react';
import { NotFound } from './NotFound';

describe('NotFound', () => {
  it('should render without crashing', () => {
    render(<NotFound />);
    expect(document.body).toBeInTheDocument();
  });
});
