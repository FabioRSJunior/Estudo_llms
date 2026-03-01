## 📌 Analisador de PDFs com IA

Aplicação web **open source** que permite upload de múltiplos PDFs, envio de prompt personalizado e processamento via LLM (local ou cloud), armazenando resultados em SQLite e exibindo tudo em uma interface web simples e organizada.

A aplicação permite ler o PDF enviado e gerar resumo, extração estruturada ou qualquer saída dinâmica em JSON com base no prompt escolhido pelo usuário.

---

# 🤖 PDF Analyzer com LLM

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Web-Flask-black)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![Ollama](https://img.shields.io/badge/LLM-Ollama-darkgreen)
![Status](https://img.shields.io/badge/Status-Open%20Source-success)

---

# 📄 Leitor Inteligente de PDFs

Infraestrutura:

Upload PDF(s)  
   ↓  
Extração de texto  
   ↓  
Chunking  
   ↓  
LLM (Groq ou Ollama)  
   ↓  
JSON estruturado  
   ↓  
SQLite  
   ↓  
Dashboard Flask  

---

## 🧠 Provedores de LLM

- **Groq** → Processamento em nuvem com alta performance.
- **Ollama** → Execução local de modelos open source.

O usuário pode selecionar o provedor diretamente na interface.

---

## 🖼️ Interface

### 📤 Tela de Submissão

- Prompt editável  
- Seleção do provedor (Groq ou Ollama)  
- Upload múltiplo de PDFs  

![Tela Submit](images/tela_submit.png)

---

### 📊 Tela de Visualização

- Lista de PDFs processados  
- Prompt utilizado  
- JSON formatado  
- Data de processamento  

![Tela Lista](images/tela_lista.png)

---

## 📂 Estrutura

- `app.py` → Aplicação Flask.
- `database.py` → Criação e manipulação do SQLite.
- `func_pdf.py` → Extração e divisão do texto.
- `llm_groq.py` → Integração com API Groq.
- `llm_ollama.py` → Integração com Ollama local.
- `templates/` → Interfaces HTML.

---

## 🚀 Como instalar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py

http://127.0.0.1:5000 
´´´

