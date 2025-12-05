"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import api from "@/src/lib/api";

export default function RegisterPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  async function handleSubmit(e: any) {
    e.preventDefault();

    await api.post("/auth/register", { email, password });

    router.push("/auth/login");
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>Registrar</h1>
      <form onSubmit={handleSubmit}>
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="email"
        />
        <br />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="senha"
        />
        <br />
        <button type="submit">Registrar</button>
      </form>
    </div>
  );
}
