import json
import sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON nao especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]

# Le os dados existentes
try:
    with open(arquivo_json, "r") as f:
        dados = json.load(f)
except FileNotFoundError:
    dados = []
except json.JSONDecodeError:
    dados = []

# Gera automaticamente o proximo ID
if dados:
    novo_id = max(int(atividade.get("id", 0)) for atividade in dados) + 1
else:
    novo_id = 1

print("========== CADASTRO DE ATIVIDADE ==========\n")
# Solicita dados ao usuario
nova = {}
nova["id"] = novo_id
nova["titulo"] = input("Digite o titulo da atividade: ")
nova["descricao"] = input("Digite a descricao: ")
nova["turmaId"] = int(input("ID da Turma: ").strip())
nova["aulaId"] = int(input("ID da aula: ").strip())
nota_txt = input("Nota (ex: 8.5): ").strip()
nova["nota"] = float(nota_txt) if nota_txt else 0.0

dados.append(nova)

# Salva novamente no arquivo JSON
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Cadastro realizado com sucesso!")
