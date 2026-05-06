import { Routes, Route } from 'react-router-dom';
import { Navigation } from './components/Navigation/Navigation';
import { Home } from './pages/Home/Home';
import { About } from './pages/About/About';
import { NotFound } from './pages/NotFound/NotFound';
import { DeveloperDirectory } from './pages/DeveloperDirectory/DeveloperDirectory';
import { DeveloperProfile } from './pages/DeveloperProfile/DeveloperProfile';

export default function App() {
  return (
    <>
      <Navigation />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/developers" element={<DeveloperDirectory />} />
          <Route path="/developers/:id" element={<DeveloperProfile />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
    </>
  );
}
