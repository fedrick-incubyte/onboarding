import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { DeveloperCard } from './DeveloperCard';

const mockDeveloper = {
  id: '1',
  name: 'Ada Lovelace',
  role: 'Frontend Engineer',
  skills: ['React', 'JavaScript'],
  location: 'London, UK',
  avatar: 'https://example.com/avatar.jpg',
};

const renderWithRouter = (ui) => render(<MemoryRouter>{ui}</MemoryRouter>);

describe('DeveloperCard', () => {
  it('should render the developer name', () => {
    renderWithRouter(<DeveloperCard developer={mockDeveloper} />);
    expect(screen.getByText('Ada Lovelace')).toBeInTheDocument();
  });

  it('should render the developer role', () => {
    renderWithRouter(<DeveloperCard developer={mockDeveloper} />);
    expect(screen.getByText('Frontend Engineer')).toBeInTheDocument();
  });

  it('should render the developer location', () => {
    renderWithRouter(<DeveloperCard developer={mockDeveloper} />);
    expect(screen.getByText('London, UK')).toBeInTheDocument();
  });

  it('should render a badge for each skill', () => {
    renderWithRouter(<DeveloperCard developer={mockDeveloper} />);
    expect(screen.getByText('React')).toBeInTheDocument();
    expect(screen.getByText('JavaScript')).toBeInTheDocument();
  });

  it('should render the developer avatar with the developer name as alt text', () => {
    renderWithRouter(<DeveloperCard developer={mockDeveloper} />);
    expect(screen.getByRole('img', { name: 'Ada Lovelace' })).toBeInTheDocument();
  });

  it('should contain a link to the developer profile page', () => {
    renderWithRouter(<DeveloperCard developer={mockDeveloper} />);
    expect(screen.getByRole('link', { name: /Ada Lovelace/i })).toHaveAttribute('href', '/developers/1');
  });
});
