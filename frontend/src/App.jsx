import React, { useState } from 'react';
import ResumeReviewForm from './components/ResumeReviewForm';
import ReviewResults from './components/ReviewResults';

function App() {
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  return (
    <div className="App" style={{ padding: 20, fontFamily: 'sans-serif' }}>
      <h1>AI Resume Reviewer</h1>

      {/* Upload form */}
      <ResumeReviewForm
        onResults={setResults}
        onError={setError}
      />

      {/* Display errors */}
      {error && (
        <p style={{ color: 'red', marginTop: 16 }}>{error}</p>
      )}

      {/* Display results */}
      {results && (
        <ReviewResults results={results} />
      )}
    </div>
  );
}

export default App;
