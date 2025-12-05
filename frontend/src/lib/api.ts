import axios from "axios";
import Cookies from "js-cookie";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// adiciona token automaticamente
api.interceptors.request.use((config) => {
  const token = Cookies.get("access_token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// tenta refresh automático
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      const refresh = Cookies.get("refresh_token");

      if (!refresh) {
        return Promise.reject(error);
      }

      try {
        const { data } = await api.post("/auth/refresh", {
          refresh_token: refresh,
        });

        Cookies.set("access_token", data.access_token);
        Cookies.set("refresh_token", data.refresh_token);

        originalRequest.headers.Authorization = `Bearer ${data.access_token}`;
        return api(originalRequest);
      } catch (err) {
        Cookies.remove("access_token");
        Cookies.remove("refresh_token");
        return Promise.reject(err);
      }
    }

    return Promise.reject(error);
  }
);

export default api;
