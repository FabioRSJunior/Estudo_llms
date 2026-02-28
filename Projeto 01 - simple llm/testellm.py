import subprocess
import time

def testar_llm():

    prompt = "Explique em 3 frases o que é inteligência artificial."

    print("Enviando prompt para LLM...")
    inicio = time.time()

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    fim = time.time()

    print("\n--- RESPOSTA ---\n")
    print(result.stdout)
    print("\nTempo total:", round(fim - inicio, 2), "segundos")


if __name__ == "__main__":
    testar_llm()