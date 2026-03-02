import sqlite3
import json
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any

from operacoes_db import criar_tabela, inserir_pessoa


DATABASE_NAME = "pessoas.db"


@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str
    observacoes: str
    dados_json: Optional[Dict[str, Any]] = None


def buscar_por_nome(nome):
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM pessoas
            WHERE nome LIKE ?
        """, (f"%{nome}%",))

        resultados = cursor.fetchall()

        pessoas = []
        for row in resultados:
            pessoa = dict(row)

            if pessoa["dados_json"]:
                pessoa["dados_json"] = json.loads(pessoa["dados_json"])

            pessoas.append(pessoa)

        return pessoas


if __name__ == "__main__":

    if __name__ == "__main__":
        criar_tabela()

        fabio = Pessoa(
            nome="Fabio Romero de Souza Junior",
            cpf="1111112",
            telefone="999999",
            observacoes="""Fabio é um engenheiro de computação movido por ambição intelectual e inquietação prática. Ele não gosta de superficialidade. Gosta de entender o porquê das coisas, desmontar sistemas, reorganizar ideias e construir soluções melhores. Seu foco é claro: inteligência artificial aplicada a problemas reais.

    Formado em Engenharia de Computação, com base técnica em eletrônica e atualmente mestrando em Engenharia Elétrica com foco em Processamento Digital de Sinais e Redes de Comunicação, Fabio constrói sua trajetória na interseção entre teoria e aplicação. Ele já trabalhou com AWS, machine learning, visão computacional, processamento de linguagem natural e integração de sistemas, sempre buscando transformar conhecimento em solução prática.

    No mestrado, desenvolve sistemas de navegação autônoma para robôs simulados utilizando ROS2, Gazebo e técnicas de Deep Reinforcement Learning. Não foge de problemas complexos — pelo contrário, tende a escolhê-los. Gosta de estruturar projetos, remover impedimentos, revisar código e organizar ambientes caóticos.

    Fabio tem um perfil analítico e estratégico. Pensa em longo prazo. Se vê concluindo um doutorado e sendo reconhecido como especialista em inteligência artificial. Ao mesmo tempo, lida com seus próprios desafios internos: oscilações de produtividade, dificuldade em dizer não, cobrança pessoal elevada. Mas ele não usa isso como desculpa — usa como ponto de melhoria.

    É organizado, responsável e gosta de planejar. Sob pressão, sua reação não é pânico: é diagnóstico. Primeiro entende a raiz do problema, depois executa.

    Fabio Romero é alguém que quer construir algo grande — não apenas em termos de carreira, mas em impacto. Ele não quer apenas trabalhar com tecnologia. Quer dominar a tecnologia.

    E no ritmo que está construindo sua base, isso não parece uma fantasia imatura. Parece um plano.
    """,
            dados_json={
                "formacao": [
                    "Engenharia de Computação",
                    "Mestrado em Engenharia Elétrica"
                ],
                "areas": [
                    "Inteligência Artificial",
                    "Machine Learning",
                    "Deep Reinforcement Learning",
                    "Visão Computacional",
                    "Processamento de Linguagem Natural"
                ],
                "ferramentas": [
                    "AWS",
                    "ROS2",
                    "Gazebo"
                ],
                "objetivo": "Tornar-se especialista em IA e concluir doutorado"
            }
        )

    inserir_pessoa(fabio)

    nova_pessoa = Pessoa(
        nome="Zyphorion Kael Dravinsky",
        cpf="222222",
        telefone="222",
        observacoes="Zyphorion é um pesquisador excêntrico especializado em sistemas complexos e arquiteturas auto-organizáveis. Possui interesse profundo em inteligência artificial, teoria do caos e simulações multiagentes. É conhecido por documentar ideias longas e detalhadas sobre futuros possíveis da tecnologia.",
        dados_json={
            "area": "Sistemas Complexos",
            "interesses": ["IA", "Simulação", "Teoria do Caos"],
            "nivel_experiencia": "Avançado"
        }
    )

    inserir_pessoa(nova_pessoa)


    print("Pessoa inserida com sucesso.")

    resultado = buscar_por_nome("Fabio")
    print(resultado)
