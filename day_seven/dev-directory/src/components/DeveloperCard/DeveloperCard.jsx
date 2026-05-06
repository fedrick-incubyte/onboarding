export function DeveloperCard({ developer }) {
  return (
    <article>
      <p>{developer.name}</p>
      <p>{developer.role}</p>
    </article>
  );
}
