import React, { useState } from 'react';
import axios from 'axios';

export default function ResumeReviewForm({ onResults, onError }) {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    onError('');
    onResults(null);

    if (!file || !jobDescription.trim()) {
      onError('Please select a PDF and enter a job description.');
      return;
    }

    const formData = new FormData();
    formData.append('resume_file', file);
    formData.append('job_description', jobDescription);

    try {
      setLoading(true);
      const { data } = await axios.post('/review', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      onResults(data);
    } catch (err) {
      const detail = err.response?.data?.detail || err.message;
      onError(detail);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: 20 }}>
      <div style={{ marginBottom: 12 }}>
        <label>
          <strong>Resume (PDF): </strong>
          <input
            type="file"
            accept="application/pdf"
            onChange={(e) => setFile(e.target.files[0])}
          />
        </label>
      </div>

      <div style={{ marginBottom: 12 }}>
        <label>
          <strong>Job Description:</strong><br/>
          <textarea
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            rows={5}
            cols={60}
          />
        </label>
      </div>

      <button type="submit" disabled={loading}>
        {loading ? 'Analyzing…' : 'Analyze Resume'}
      </button>
    </form>
  );
}
