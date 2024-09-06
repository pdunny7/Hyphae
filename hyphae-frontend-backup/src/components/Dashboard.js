import React, { useState, useEffect } from 'react';
import { getMycologicalData } from '../services/api';

function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await getMycologicalData();
        setData(result.data);
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      <h2>Mycological Data Dashboard</h2>
      <table>
        <thead>
          <tr>
            <th>Species</th>
            <th>Strain</th>
            <th>Collection Date</th>
            <th>Location</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td>{item.species}</td>
              <td>{item.strain}</td>
              <td>{new Date(item.collection_date).toLocaleDateString()}</td>
              <td>{item.location}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;