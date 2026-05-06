import { render, screen } from '@testing-library/react';
import { MemoryRouter, Routes, Route } from 'react-router-dom';
import { DeveloperProfile } from './DeveloperProfile';

const renderAtRoute = (path) =>
  render(
    <MemoryRouter initialEntries={[path]}>
      <Routes>
        <Route path="/developers/:id" element={<DeveloperProfile />} />
      </Routes>
    </MemoryRouter>
  );

describe('DeveloperProfile', () => {
  it('should render the developer name from the URL param', () => {
    renderAtRoute('/developers/1');
    expect(screen.getByRole('heading', { name: /ada lovelace/i })).toBeInTheDocument();
  });

  it('should render the developer bio', () => {
    renderAtRoute('/developers/1');
    expect(screen.getByText(/pioneer of component-based thinking/i)).toBeInTheDocument();
  });

  it('should render all skills as badges', () => {
    renderAtRoute('/developers/1');
    expect(screen.getByText('React')).toBeInTheDocument();
    expect(screen.getByText('JavaScript')).toBeInTheDocument();
    expect(screen.getByText('CSS')).toBeInTheDocument();
  });

  it('should render a back link to the developer directory', () => {
    renderAtRoute('/developers/1');
    expect(screen.getByRole('link', { name: /back/i })).toBeInTheDocument();
  });

  it('should show a not found message for an unknown id', () => {
    renderAtRoute('/developers/999');
    expect(screen.getByText(/developer not found/i)).toBeInTheDocument();
  });
});
