"use client";

import { createContext, useContext, useEffect, useState } from "react";
import api from "../lib/api";
import Cookies from "js-cookie";

interface User {
  id: number;
  email: string;
  plan: string;
  created_at: string;
}

interface AuthContextData {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextData>({} as AuthContextData);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // tenta carregar usuário automaticamente
  useEffect(() => {
    const token = Cookies.get("access_token");

    if (!token) {
      setLoading(false);
      return;
    }

    api
      .get("/auth/me")
      .then((res) => setUser(res.data))
      .finally(() => setLoading(false));
  }, []);

  async function login(email: string, password: string) {
    const res = await api.post("/auth/login", { email, password });

    Cookies.set("access_token", res.data.access_token);
    Cookies.set("refresh_token", res.data.refresh_token);

    const me = await api.get("/auth/me");
    setUser(me.data);
  }

  function logout() {
    Cookies.remove("access_token");
    Cookies.remove("refresh_token");
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
