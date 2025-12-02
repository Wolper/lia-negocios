// frontend/app/login/page.tsx
"use client";

import { FormEvent, useState } from "react";
import Link from "next/link";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    // Módulo 1: ainda não vamos chamar o backend de verdade.
    // Apenas simulamos um submit.
    console.log("Login submit:", { email, senha });
    alert("No próximo módulo, vamos conectar este login ao backend.");
  }

  return (
    <main className="min-h-screen bg-slate-950 text-slate-50 flex items-center justify-center">
      <div className="w-full max-w-md rounded-2xl border border-slate-800 bg-slate-900/60 px-6 py-8">
        <header className="mb-6 text-center">
          <h1 className="text-xl font-semibold mb-1">Entrar na LIA Negócios</h1>
          <p className="text-xs text-slate-400">
            Faça login para acessar sua assistente inteligente.
          </p>
        </header>

        <form className="space-y-4" onSubmit={handleSubmit}>
          <div>
            <label className="block text-xs font-medium mb-1" htmlFor="email">
              E-mail
            </label>
            <input
              id="email"
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm outline-none focus:border-emerald-400"
              placeholder="voce@exemplo.com"
            />
          </div>

          <div>
            <label className="block text-xs font-medium mb-1" htmlFor="senha">
              Senha
            </label>
            <input
              id="senha"
              type="password"
              required
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
              className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm outline-none focus:border-emerald-400"
              placeholder="••••••••"
            />
          </div>

          <button
            type="submit"
            className="w-full rounded-full bg-emerald-500 py-2 text-sm font-semibold text-slate-950 hover:bg-emerald-400"
          >
            Entrar
          </button>
        </form>

        <p className="mt-4 text-center text-xs text-slate-400">
          Ainda não tem conta?{" "}
          <span className="text-emerald-400">
            No próximo módulo, vamos criar o fluxo de cadastro.
          </span>
        </p>

        <p className="mt-2 text-center text-xs">
          <Link href="/" className="text-slate-400 hover:text-emerald-400">
            Voltar para a página inicial
          </Link>
        </p>
      </div>
    </main>
  );
}
