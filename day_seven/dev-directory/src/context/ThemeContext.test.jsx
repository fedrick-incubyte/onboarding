import { render, screen, fireEvent } from '@testing-library/react';
import { ThemeProvider, useTheme } from './ThemeContext';

function TestConsumer() {
  const { theme, toggleTheme } = useTheme();
  return (
    <>
      <span>{theme}</span>
      <button onClick={toggleTheme}>Toggle</button>
    </>
  );
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

  it('should toggle the theme from light to dark', () => {
    render(
      <ThemeProvider>
        <TestConsumer />
      </ThemeProvider>
    );
    fireEvent.click(screen.getByRole('button', { name: /toggle/i }));
    expect(screen.getByText('dark')).toBeInTheDocument();
  });

  it('should toggle the theme back to light on a second click', () => {
    render(
      <ThemeProvider>
        <TestConsumer />
      </ThemeProvider>
    );
    fireEvent.click(screen.getByRole('button', { name: /toggle/i }));
    fireEvent.click(screen.getByRole('button', { name: /toggle/i }));
    expect(screen.getByText('light')).toBeInTheDocument();
  });

  it('should throw when useTheme is used outside a ThemeProvider', () => {
    expect(() => render(<TestConsumer />)).toThrow();
  });

  it('should set data-theme attribute on document body', () => {
    render(
      <ThemeProvider>
        <TestConsumer />
      </ThemeProvider>
    );
    expect(document.body.getAttribute('data-theme')).toBe('light');
  });
});
