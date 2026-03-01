

## 📌 Agente de Busca de Editais com IA

Projeto que automatiza a busca de editais relacionados a Inteligência Artificial, realiza scraping das páginas, utiliza LLM local via Ollama para extrair e resumir informações relevantes e gera um relatório final em HTML.


# 🤖 Agente de Editais com IA

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)
![BeautifulSoup](https://img.shields.io/badge/Scraping-BeautifulSoup-green)
![Jinja2](https://img.shields.io/badge/Template-Jinja2-red)

# Agente de Busca de Editais


infra; 

Query
   ↓
Search → lista de links
   ↓
Loop
   ↓
Scrape HTML
   ↓
LLM (resumo/extração)
   ↓
Append resultado
   ↓
Gerar relatório HTML


## 📂 Estrutura

- `main.py` → Orquestra todo o fluxo do sistema.
- `search.py` → Realiza a busca dos editais na web.
- `scraper.py` → Faz scraping das páginas e extrai o conteúdo HTML.
- `summarizer.py` → Envia o texto para a LLM via Ollama para resumo/extração.
- `report.py` → Gera o relatório final em HTML usando template.
- `templates/report.html` → Template base para renderização do relatório.


---

## 📂 Estrutura

- `main.py` → Orquestra todo o fluxo do sistema.
- `search.py` → Realiza a busca dos editais na web.
- `scraper.py` → Faz scraping das páginas e extrai o conteúdo HTML.
- `summarizer.py` → Envia o texto para a LLM via Ollama para resumo/extração.
- `report.py` → Gera o relatório final em HTML usando template.
- `templates/report.html` → Template base para renderização do relatório.

---

## 🚀 Instalação

Crie o ambiente virtual e instale as dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
