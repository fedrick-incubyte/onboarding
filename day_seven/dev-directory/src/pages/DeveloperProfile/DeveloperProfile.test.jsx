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
  it('should render without crashing', () => {
    renderAtRoute('/developers/1');
    expect(document.body).toBeInTheDocument();
  });
});
