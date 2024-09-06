import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const login = async (username, password) => {
  const response = await axios.post(`${API_URL}/auth/token`, {
    username,
    password,
  });
  return response.data;
};

export const getMycologicalData = async () => {
  const token = localStorage.getItem('token');
  const response = await axios.get(`${API_URL}/data/mycological-data`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};