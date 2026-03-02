<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-Agent-green" />
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-black" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Execution-100%25%20Offline-success" />
</p>

# Projeto Simples de Teste — Agente LangChain (Offline)

Este é um projeto simples de teste de um agente utilizando **LangChain**, rodando totalmente offline.

A proposta foi validar se um agente conectado a um banco SQLite seria capaz de:

- Interpretar uma pergunta em linguagem natural  
- Gerar automaticamente uma consulta SQL  
- Executar essa consulta na tabela  
- Retornar a resposta corretamente  

Tudo isso sem que funções específicas de busca tivessem sido implementadas manualmente.

---

## Exemplo de Execução

A pergunta gerou automaticamente uma consulta na tabela.

**Pergunta:**

Pergunta: quais interesses em comum de fabio e Zyphor ?

**Resposta:**
The common interests between Fabio and Zyphor are
"Inteligência Artificial",
"Machine Learning",
"Deep Reinforcement Learning",
"Visão Computacional", and
"Processamento de Linguagem Natural".

**conclusão:**

Isso demonstra que o agente conseguiu interpretar a pergunta, identificar onde a informação estava armazenada e consultar o banco de dados corretamente.

<!--
## ⚙️ Arquitetura

- LLM local rodando via Ollama
- Banco de dados SQLite
- SQL Agent do LangChain
- Execução totalmente offline

O agente recebe o schema do banco, decide qual consulta SQL deve ser feita, executa a query e retorna o resultado formatado em linguagem natural.
-->

---

<!--
## 🚀 Conclusão

Mesmo sendo um projeto simples, ele demonstra um ponto importante:

O agente foi capaz de buscar dados no banco de dados sem ter sido explicitamente programado para isso.

Não foi criada uma função como buscar_profissao().
O modelo gerou a consulta dinamicamente com base na estrutura da tabela.

Isso mostra o potencial de agentes LLM atuando como uma camada inteligente sobre bancos de dados estruturados, operando 100% localmente e com controle total do ambiente.
-->
