"use client";

import { useAuth } from "@/src/context/AuthContext";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function Dashboard() {
  const { user, loading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!loading && !user) {
      router.push("/auth/login");
    }
  }, [loading, user]);

  if (loading || !user) return <p>Carregando...</p>;

  return (
    <div style={{ padding: 40 }}>
      <h1>Bem vindo, {user.email}</h1>
      <p>Seu plano: {user.plan}</p>
    </div>
  );
}
