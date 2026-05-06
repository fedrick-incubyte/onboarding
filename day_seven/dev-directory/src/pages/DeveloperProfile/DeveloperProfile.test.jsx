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
});
