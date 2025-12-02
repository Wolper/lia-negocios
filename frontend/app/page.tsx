// frontend/app/page.tsx
import Link from "next/link";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-50">
      <div className="mx-auto max-w-4xl px-4 py-12">
        {/* Header simples */}
        <header className="flex items-center justify-between mb-12">
          <div className="flex items-center gap-2">
            <span className="inline-flex h-9 w-9 items-center justify-center rounded-full bg-emerald-500 font-bold">
              L
            </span>
            <div>
              <h1 className="text-lg font-semibold">LIA Negócios</h1>
              <p className="text-xs text-slate-400">
                Uma solução MM AI Studio
              </p>
            </div>
          </div>

          <nav className="flex items-center gap-4 text-sm">
            <Link href="#planos" className="hover:text-emerald-400">
              Planos
            </Link>
            <Link href="/login" className="hover:text-emerald-400">
              Entrar
            </Link>
          </nav>
        </header>

        {/* Hero */}
        <section className="mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Sua assistente inteligente para pequenos negócios.
          </h2>
          <p className="text-slate-300 mb-6 max-w-xl">
            A LIA Negócios te ajuda a criar posts, responder clientes e montar
            ofertas em poucos cliques, usando IA de um jeito simples e em
            português.
          </p>

          <div className="flex flex-wrap items-center gap-4">
            <Link
              href="/login"
              className="inline-flex items-center justify-center rounded-full bg-emerald-500 px-6 py-2 text-sm font-semibold text-slate-950 hover:bg-emerald-400"
            >
              Começar grátis
            </Link>
            <Link
              href="#planos"
              className="text-sm text-slate-300 hover:text-emerald-400"
            >
              Ver planos
            </Link>
          </div>
        </section>

        {/* Planos (versão simplificada do que já fizemos) */}
        <section id="planos" className="mb-16">
          <h3 className="text-2xl font-semibold mb-4">Planos</h3>
          <p className="text-slate-300 mb-6">
            Comece grátis e evolua para um plano que acompanha o crescimento do
            seu negócio.
          </p>

          <div className="grid gap-6 md:grid-cols-3">
            {/* Free */}
            <div className="rounded-xl border border-slate-800 p-4">
              <h4 className="font-semibold mb-1">Free – Starter</h4>
              <p className="text-sm text-slate-400 mb-2">
                Perfeito para começar a usar IA sem custo.
              </p>
              <p className="text-xl font-bold mb-1">R$ 0/mês</p>
              <ul className="text-sm text-slate-300 space-y-1 mb-4">
                <li>• Chat com IA em português</li>
                <li>• Modelo rápido e econômico</li>
                <li>• Até 50 mensagens/mês</li>
              </ul>
              <Link
                href="/login"
                className="inline-flex w-full items-center justify-center rounded-full border border-slate-500 px-4 py-2 text-sm font-semibold hover:border-emerald-400 hover:text-emerald-300"
              >
                Começar grátis
              </Link>
            </div>

            {/* Pro */}
            <div className="rounded-xl border border-emerald-500 bg-slate-900 p-4 shadow-lg">
              <h4 className="font-semibold mb-1">Pro – Profissional</h4>
              <p className="text-sm text-slate-300 mb-2">
                A IA como parceira diária do seu negócio.
              </p>
              <p className="text-xl font-bold mb-1">R$ 39,90/mês</p>
              <p className="text-xs text-emerald-300 mb-2">
                Lançamento: R$ 29,90/mês para os primeiros assinantes.
              </p>
              <ul className="text-sm text-slate-200 space-y-1 mb-4">
                <li>• Tudo do plano Free</li>
                <li>• Modelos premium de IA</li>
                <li>• Até 300 mensagens/mês</li>
                <li>• Templates avançados e histórico estendido</li>
              </ul>
              <Link
                href="/login"
                className="inline-flex w-full items-center justify-center rounded-full bg-emerald-500 px-4 py-2 text-sm font-semibold text-slate-950 hover:bg-emerald-400"
              >
                Assinar plano Pro
              </Link>
            </div>

            {/* Business */}
            <div className="rounded-xl border border-slate-800 p-4">
              <h4 className="font-semibold mb-1">
                Business – Time &amp; Agência
              </h4>
              <p className="text-sm text-slate-400 mb-2">
                Ideal para equipes, agências e empresas.
              </p>
              <p className="text-xl font-bold mb-1">
                A partir de R$ 99,90/mês
              </p>
              <ul className="text-sm text-slate-300 space-y-1 mb-4">
                <li>• Até 3 usuários</li>
                <li>• Cota ampliada de mensagens</li>
                <li>• Organização por clientes/projetos</li>
              </ul>
              <button className="inline-flex w-full items-center justify-center rounded-full border border-slate-500 px-4 py-2 text-sm font-semibold hover:border-emerald-400 hover:text-emerald-300">
                Falar com o time comercial
              </button>
            </div>
          </div>
        </section>

        {/* Rodapé */}
        <footer className="border-t border-slate-800 pt-4 text-xs text-slate-500">
          © {new Date().getFullYear()} LIA Negócios · MM AI Studio
        </footer>
      </div>
    </main>
  );
}
