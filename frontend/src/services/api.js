import axios from 'axios';

// Create an Axios instance with default configuration
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || `http://${window.location.hostname}:8000`,
  headers: {
    'Content-Type': 'application/json',
  },
  // Removed withCredentials to fix CORS issues with external access
  // withCredentials: true,
});

// Add a request interceptor for handling auth tokens, etc.
api.interceptors.request.use(
  (config) => {
    // You can add auth tokens or other headers here
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Add a response interceptor for handling errors
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // Handle specific error cases here
    if (error.response) {
      // Server responded with a status code outside the 2xx range
      console.error('API Error:', error.response.data);
    } else if (error.request) {
      // The request was made but no response was received
      console.error('API Error: No response received');
    } else {
      // Something else happened while setting up the request
      console.error('API Error:', error.message);
    }
    return Promise.reject(error);
  }
);

export default api; 