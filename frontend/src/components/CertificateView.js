import React, { useState, useEffect } from 'react';

const CertificateView = ({ traineeId }) => {
  const [trainee, setTrainee] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/api/trainees/${traineeId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setTrainee(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setError(error);
        setLoading(false);
      });
  }, [traineeId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      {trainee && (
        <div>
          <h2>{trainee.name}</h2>
          <p>Course: {trainee.course}</p>
          <p>Certified Date: {trainee.certified_date}</p>
          {trainee.certificate && (
            <img src={trainee.certificate} alt="Certificate" style={{ maxWidth: '100%' }} />
          )}
        </div>
      )}
    </div>
  );
};

export default CertificateView;
