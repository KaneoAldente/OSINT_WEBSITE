import { useRouter } from 'next/router';
import { useState } from 'react';
import useSWR from 'swr';

const fetcher = (url) => fetch(url).then((res) => res.json());

export default function IndicatorDetail() {
  const router = useRouter();
  const { id } = router.query;
  const { data, error } = useSWR(
    id ? `http://localhost:8000/indicators` : null,
    fetcher
  );
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  if (error) return <div>Error loading indicator</div>;
  if (!data) return <div>Loading...</div>;
  const indicator = data.indicators.find((ind) => ind.id === id);
  if (!indicator) return <div>Indicator not found</div>;

  async function handleEvaluate() {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/event', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ indicator_id: id, payload: {} }),
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setResult({ error: err.message });
    }
    setLoading(false);
  }

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Indicator {indicator.id}</h1>
      <p><strong>Description:</strong> {indicator.description}</p>
      <p><strong>PIR:</strong> {indicator.pir}</p>
      <p><strong>Course of action:</strong> {indicator.coa}</p>
      <p><strong>Data signals:</strong> {indicator.data_signals.join(', ')}</p>
      <button onClick={handleEvaluate} disabled={loading} style={{ marginTop: '1rem', padding: '0.5rem 1rem' }}>
        {loading ? 'Evaluating…' : 'Simulate Event'}
      </button>
      {result && (
        <div style={{ marginTop: '1rem' }}>
          <h2>Evaluation Result</h2>
          {result.error ? (
            <p style={{ color: 'red' }}>Error: {result.error}</p>
          ) : (
            <pre style={{ background: '#f0f0f0', padding: '1rem' }}>{JSON.stringify(result, null, 2)}</pre>
          )}
        </div>
      )}
    </div>
  );
}