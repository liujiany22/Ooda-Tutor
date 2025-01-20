// src/api/api.js

import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:7777';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  // 可以在此设置请求头
  return config;
}, (error) => {
  return Promise.reject(error);
});

// 响应拦截器：可以在此统一处理响应
api.interceptors.response.use((response) => {
  return response.data;
}, (error) => {
  return Promise.reject(error);
});

export default api;
