# 🧠 Estudos e Projetos com LLMs

Repositório dedicado a experimentos práticos utilizando Large Language Models (LLMs), com foco em aplicações reais, automação de tarefas e geração de conteúdo estruturado.

---

## 📂 Projetos

### 📌 Projeto 01 — Agente de Busca de Editais com IA
🔗 [Acessar projeto](https://github.com/FabioRSJunior/Estudo_llms/tree/main/Projeto%2001%20-%20simple%20llm)

Sistema que automatiza a busca de editais relacionados a Inteligência Artificial.  
Realiza scraping de páginas, utiliza LLM local via Ollama para extrair e resumir informações relevantes e gera um relatório final em HTML.

**Conceitos explorados:**
- Integração com LLM local
- Prompt engineering
- Extração estruturada de informação
- Geração automática de relatórios

---

<!-- MODELO PARA NOVOS PROJETOS -->

### 📌 Projeto 02 — Analisador de PDFs com IA
🔗 [Acessar projeto](https://github.com/FabioRSJunior/Estudo_llms/tree/main/Projeto%2002%20-%20Sistema%20Groq%20Ollm)

O projeto permite gerar resumos, extrações estruturadas ou qualquer saída dinâmica orientada por prompt, explorando integração entre backend web, processamento de documentos e modelos de linguagem.

**Conceitos explorados:**
- Pipeline de processamento de documentos 
- Engenharia de prompt aplicada a PDFs
- Integração com LLM via API (Groq) e execução local com Ollama
- Geração de JSON estruturado a partir de linguagem natural
- Persistência de dados com SQLite
- Desenvolvimento de aplicação web com Flask
- Separação modular de responsabilidades (arquitetura em camadas)
 
---

### 📌 Projeto 03 — Agente LangChain Offline com SQLite  
🔗 [Acessar projeto](https://github.com/FabioRSJunior/Estudo_llms/tree/main/Projeto%2003%20-%20introdu%C3%A7%C3%A3o%20a%20Agentes)

Projeto simples de validação de um agente construído com LangChain, rodando totalmente offline.  

A proposta foi testar se um agente conectado a um banco SQLite conseguiria interpretar perguntas em linguagem natural, gerar automaticamente a consulta SQL correspondente, executar a query e retornar a resposta correta — tudo isso sem funções de busca implementadas manualmente.

**Conceitos explorados:**
- Arquitetura de agentes com LangChain  
- Integração LLM + banco de dados SQLite  
- Geração automática de SQL via linguagem natural  
- Execução dinâmica de consultas  
- Orquestração de ferramentas (tools) pelo agente  

---


## 🎯 Objetivo do Repositório

- Explorar aplicações práticas de LLMs
- Testar modelos locais e APIs
- Evoluir pipelines inteligentes
- Construir base técnica para futuros sistemas multiagente
