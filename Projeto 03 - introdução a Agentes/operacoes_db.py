import sqlite3
import json
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


DATABASE_NAME = "pessoas.db"


# =========================
# Modelo de Domínio
# =========================
@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str
    observacoes: str
    dados_json: Optional[Dict[str, Any]] = None


# =========================
# Inicialização do Banco
# =========================
def criar_tabela() -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE,
                telefone TEXT NOT NULL,
                observacoes TEXT,
                dados_json TEXT
            )
        """)
        conn.commit()


# =========================
# Inserção de Dados
# =========================
def inserir_pessoa(pessoa: Pessoa) -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()

        json_serializado = (
            json.dumps(pessoa.dados_json, ensure_ascii=False)
            if pessoa.dados_json else None
        )

        cursor.execute("""
            INSERT INTO pessoas (nome, cpf, telefone, observacoes, dados_json)
            VALUES (?, ?, ?, ?, ?)
        """, (
            pessoa.nome,
            pessoa.cpf,
            pessoa.telefone,
            pessoa.observacoes,
            json_serializado
        ))

        conn.commit()


# =========================
# Consulta com retorno em JSON CPF 
# =========================
def buscar_pessoa_por_cpf(cpf: str) -> Optional[Dict[str, Any]]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pessoas WHERE cpf = ?", (cpf,))
        row = cursor.fetchone()

        if row:
            resultado = dict(row)
            if resultado["dados_json"]:
                resultado["dados_json"] = json.loads(resultado["dados_json"])
            return resultado

        return None
    

# =========================
# Consulta com retorno em JSON NOME
# =========================
def buscar_pessoa_por_nome(nome: str) -> Optional[Dict[str, Any]]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pessoas WHERE nome = ?", (nome,))
        row = cursor.fetchone()

        if row:
            resultado = dict(row)
            if resultado["dados_json"]:
                resultado["dados_json"] = json.loads(resultado["dados_json"])
            return resultado

        return None






   