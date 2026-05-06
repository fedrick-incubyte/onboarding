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

  it('should render the developer role', () => {
    render(<DeveloperCard developer={mockDeveloper} />);
    expect(screen.getByText('Frontend Engineer')).toBeInTheDocument();
  });

  it('should render the developer location', () => {
    render(<DeveloperCard developer={mockDeveloper} />);
    expect(screen.getByText('London, UK')).toBeInTheDocument();
  });
});
