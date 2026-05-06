import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';

vi.mock('../../data/developers', () => ({ developers: [] }));

const { DeveloperDirectory } = await import('./DeveloperDirectory');

describe('DeveloperDirectory — empty state', () => {
  it('should show a no developers found message when no developers match the filter', () => {
    render(<MemoryRouter><DeveloperDirectory /></MemoryRouter>);
    expect(screen.getByText('No developers found')).toBeInTheDocument();
  });
});
