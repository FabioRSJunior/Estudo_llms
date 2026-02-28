from search_2 import search_editais_2
from scraper import scrape_page
from summarizer import summarize_text
from report import generate_report
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def main():
    query = "edital inteligência artificial"
    
    logging.info("Iniciando busca...")
    results = search_editais_2(query)
    logging.info(f"{len(results)} resultados encontrados")

    processed = []

    for i, r in enumerate(results, 1):
        logging.info(f"[{i}/{len(results)}] Processando: {r['title']}")

        start = time.time()

        logging.info("Baixando página...")
        content = scrape_page(r["href"])
        logging.info(f"Conteúdo coletado ({len(content)} caracteres)")

        logging.info("Gerando resumo com LLM...")
        summary = summarize_text(content)

        elapsed = time.time() - start
        logging.info(f"Concluído em {elapsed:.2f}s")

        processed.append({
            "title": r["title"],
            "link": r["href"],
            "summary": summary
        })

    logging.info("Gerando relatório HTML...")
    generate_report(processed)

    logging.info("Relatório gerado com sucesso!")

if __name__ == "__main__":
    main()


""" from search_2 import search_editais_2
from scraper import scrape_page
from summarizer import summarize_text
from report import generate_report

def main():
    query = "edital inteligência artificial 2026 bolsa mestrado doutorado"
    
    results = search_editais_2(query)

    processed = []

    for r in results:
        print(f"Processando: {r['title']}")
        
        content = scrape_page(r["href"])
        summary = summarize_text(content)

        processed.append({
            "title": r["title"],
            "link": r["href"],
            "summary": summary
        })

    generate_report(processed)
    print("Relatório gerado: relatorio.html")

if __name__ == "__main__":
    main() """