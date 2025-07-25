import useSWR from 'swr';
import Link from 'next/link';

const fetcher = (url) => fetch(url).then((res) => res.json());

export default function Home() {
  const { data, error } = useSWR('http://localhost:8000/indicators', fetcher);

  if (error) return <div>Failed to load indicators</div>;
  if (!data) return <div>Loading...</div>;

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>OSINT Warning Dashboard</h1>
      <p>This prototype lists available indicators and links to detail pages.</p>
      <ul>
        {data.indicators.map((ind) => (
          <li key={ind.id} style={{ marginBottom: '0.5rem' }}>
            <Link href={`/indicator/${ind.id}`}>
              {ind.id}: {ind.description}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}