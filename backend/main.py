# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LIA Negócios API - Módulo 1")

# Em Módulo 1, libera CORS para facilitar testes locais
origins = [
    "http://localhost:3000",  # frontend Next.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "LIA Negócios API - Módulo 1 rodando"}


@app.post("/fake-login")
def fake_login():
    # Módulo 1: apenas um endpoint de teste
    return {"detail": "No próximo módulo, vamos implementar login de verdade"}
