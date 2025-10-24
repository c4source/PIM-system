import json
import sys
import hashlib
import getpass

def gerar_hash_senha(senha):
    """ 
    Gera um hash SHA-256 para a senha
    
    Args:
        senha (str): A senha em texto puro do aluno.
    
    Returns: 
        str: O hash SHA-256 da senha     
    
    """     
    return hashlib.sha256(senha.encode()).hexdigest()


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



# Gera automaticamente o proximo ID
if dados:
    novo_id = max(int(administrador.get("id", 0)) for administrador in dados) + 1
else:
    novo_id = 1

print("========== CADASTRO DE ADMINISTRADOR ==========\n")
# Solicita dados ao usuario
novo = {}
novo["id"] = novo_id
novo["nome"] = input("Digite o nome: ")
novo["email"] = input("Digite seu e-mail: ")
senha_plana = getpass.getpass("Crie uma senha: ")
novo["senha"] = hashlib.sha256(senha_plana.encode()).hexdigest()

dados.append(novo)

# Salva novamente no arquivo JSON
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print(f"\nCadastro realizado com sucesso!")
