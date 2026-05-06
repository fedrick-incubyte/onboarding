import { render, screen } from '@testing-library/react';
import { DeveloperCard } from './DeveloperCard';

const mockDeveloper = {
  id: '1',
  name: 'Ada Lovelace',
  role: 'Frontend Engineer',
  skills: ['React', 'JavaScript'],
  location: 'London, UK',
  avatar: 'https://example.com/avatar.jpg',
};

describe('DeveloperCard', () => {
  it('should render the developer name', () => {
    render(<DeveloperCard developer={mockDeveloper} />);
    expect(screen.getByText('Ada Lovelace')).toBeInTheDocument();
  });
});
