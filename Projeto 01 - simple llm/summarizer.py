import subprocess
import json

def summarize_text(text):
    prompt = f"""
    Resuma o edital abaixo destacando:
    - Número do edital
    - Instituição
    - Público-alvo
    - Prazo
    - Área

    Texto:
    {text}
    """

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout