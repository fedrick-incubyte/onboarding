import { render, screen, fireEvent } from '@testing-library/react';
import { ThemeProvider, useTheme } from '../../context/ThemeContext';
import { ThemeToggle } from './ThemeToggle';

function ThemeDisplay() {
  const { theme } = useTheme();
  return <span>{theme}</span>;
}

describe('ThemeToggle', () => {
  it('should render a toggle button', () => {
    render(
      <ThemeProvider>
        <ThemeToggle />
      </ThemeProvider>
    );
    expect(screen.getByRole('button', { name: /toggle theme/i })).toBeInTheDocument();
  });

  it('should call toggleTheme from context when clicked', () => {
    render(
      <ThemeProvider>
        <ThemeDisplay />
        <ThemeToggle />
      </ThemeProvider>
    );
    fireEvent.click(screen.getByRole('button', { name: /toggle theme/i }));
    expect(screen.getByText('dark')).toBeInTheDocument();
  });
});
