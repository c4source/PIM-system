import json
import sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON nao especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]

try:
    print("==========LISTA DE PROFESSORES CADASTRADOS==========")
    with open(arquivo_json, "r") as f:
        dados = json.load(f)
        # Imprime cada item do JSON de forma legivel
        for item in dados:
            for chave, valor in item.items():
                print(f"{chave}: {valor}")
            print("-" * 20)
except FileNotFoundError:
    print("Arquivo nao encontrado:", arquivo_json)
except json.JSONDecodeError:
    print("Erro ao ler JSON:", arquivo_json)
