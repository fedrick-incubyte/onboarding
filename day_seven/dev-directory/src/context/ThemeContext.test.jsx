import { render, screen } from '@testing-library/react';
import { ThemeProvider, useTheme } from './ThemeContext';

function TestConsumer() {
  const { theme } = useTheme();
  return <span>{theme}</span>;
}

describe('ThemeContext', () => {
  it('should provide a default theme of light', () => {
    render(
      <ThemeProvider>
        <TestConsumer />
      </ThemeProvider>
    );
    expect(screen.getByText('light')).toBeInTheDocument();
  });
});
