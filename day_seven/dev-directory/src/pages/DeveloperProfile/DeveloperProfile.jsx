import { useParams } from 'react-router-dom';
import { developers } from '../../data/developers';

export function DeveloperProfile() {
  const { id } = useParams();
  const developer = developers.find((d) => d.id === id);

  return <h1>{developer.name}</h1>;
}
