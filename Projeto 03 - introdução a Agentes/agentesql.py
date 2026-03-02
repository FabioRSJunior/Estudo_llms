from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_ollama import ChatOllama

# Conexão com SQLite
db = SQLDatabase.from_uri("sqlite:///pessoas.db")

# Modelo local via Ollama
llm = ChatOllama(
    model="llama3",
    temperature=0
)

# Criando agente SQLS
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)

if __name__ == "__main__":
    while True:
        pergunta = input("\nPergunta: ")
        if pergunta.lower() in ["sair", "exit"]:
            break

        resposta = agent_executor.invoke({"input": pergunta})
        print("\nResposta:", resposta["output"])