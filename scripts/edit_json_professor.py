import json
import sys
import hashlib
import getpass

def gerar_hash_senha(senha):
    """ 
    Gera um hash SHA-256 para a senha
    
    Args:
        senha (str): A senha em texto puro do professor.
    
    Returns: 
        str: O hash SHA-256 da senha     
    """
    return hashlib.sha256(senha.encode()).hexdigest()


if len(sys.argv) < 2:
    print("Erro: arquivo JSON nao especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]

try:
    with open(arquivo_json, "r") as f:
        dados = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    print("Erro: arquivo nao encontrado ou vazio.")
    sys.exit(1)

print("========== EDIÇÃO DE PROFESSOR ==========\n")
id_alvo = input("Digite o ID do professor que deseja editar: ").strip()

# procura professor pelo id
professor = None
for item in dados:
    if str(item.get("id")) == id_alvo:
        professor = item
        break

if professor is None:
    print("Professor nao encontrado.")
    sys.exit(1)

print(f"Editando professor ID {professor['id']} - {professor['nome']}")

novo_nome = input("Novo nome (Enter para manter): ").strip()
novo_email = input("Novo e-mail (Enter para manter): ").strip()
nova_senha = getpass.getpass("Novo senha (Enter para manter): ").strip()

if novo_nome:
    professor["nome"] = novo_nome
if novo_email:
    professor["email"] = novo_email
if nova_senha:
    professor["senha"] = gerar_hash_senha(nova_senha)

# salva alteracoes
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Registro atualizado com sucesso!")
