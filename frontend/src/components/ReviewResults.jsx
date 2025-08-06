import React from 'react';

export default function ReviewResults({ results }) {
  const { score, missing_keywords, suggestions } = results;

  return (
    <div style={{ marginTop: 24 }}>
      <h2>Results</h2>
      <p>
        <strong>Match Score:</strong>{' '}
        {(score * 100).toFixed(1)}%
      </p>

      {missing_keywords.length > 0 && (
        <div style={{ marginTop: 12 }}>
          <h3>Missing Keywords</h3>
          <ul>
            {missing_keywords.map((kw, i) => (
              <li key={i}>{kw}</li>
            ))}
          </ul>
        </div>
      )}

      {suggestions.length > 0 && (
        <div style={{ marginTop: 12 }}>
          <h3>Suggestions</h3>
          <ul>
            {suggestions.map((sug, i) => (
              <li key={i}>{sug}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
