// frontend/src/components/TraineeList.js
import React, { useEffect, useState } from 'react';

const TraineeList = () => {
    const [trainees, setTrainees] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/api/trainees')
            .then(response => response.json())
            .then(data => setTrainees(data))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div>
            {trainees.map(trainee => (
                <div key={trainee.id}>{trainee.name}</div>
            ))}
        </div>
    );
};

export default TraineeList;
