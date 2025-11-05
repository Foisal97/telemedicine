import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const signup = async (email: string, password: string) => {
  return axios.post(`${API_URL}/auth/signup`, { email, password });
};

export const login = async (email: string, password: string) => {
  return axios.post(`${API_URL}/auth/login`, { email, password });
};
