import React, { useEffect, useState } from 'react';
import Calendar from 'react-calendar';
import axios from 'axios';

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/events')
      .then(response => {
        setEvents(response.data);
      });
  }, []);

  return (
    <div>
      <h1>Календар</h1>
      <Calendar />
      {/* Тут можна додати логіку для відображення подій */}
    </div>
  );
}

export default App;
