import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

// Create axios instance with credentials enabled for cookie support
const axiosInstance = axios.create({
  baseURL: API_URL,
  withCredentials: true,
});

export const signup = async (email: string, password: string) => {
  return axiosInstance.post("/auth/signup", { email, password });
};

export const login = async (email: string, password: string) => {
  return axiosInstance.post("/auth/login", { email, password });
};

export const refreshAccessToken = async (refresh_token: string) => {
  return axiosInstance.post("/auth/refresh", { refresh_token });
};
