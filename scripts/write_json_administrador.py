import json
import sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON nao especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]

# Le os dados existentes, se o arquivo existir
try:
    with open(arquivo_json, "r") as f:
        dados = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    dados = []

print("========== CADASTRO DE ADMINISTRADOR ==========\n")

# Gera automaticamente o proximo ID
if dados:
    novo_id = max(int(administrador.get("id", 0)) for administrador in dados) + 1
else:
    novo_id = 1

# Solicita dados ao usuario
novo = {}
novo["id"] = novo_id
novo["nome"] = input("Digite o nome: ")
novo["cargo"] = input("Digite o cargo: ")
novo["usuario"] = input("Digite o seu usuario: ")
novo["senha"] = input("Crie uma senha: ")


dados.append(novo)

# Salva novamente no arquivo JSON
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print(f"\nAdministrador cadastrado com sucesso! ID gerado automaticamente: {novo_id}")
