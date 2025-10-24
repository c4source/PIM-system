import json
import sys
import os
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
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]
turmas_json = os.path.join(os.path.dirname(arquivo_json), "turmas.json")

# --- Funções utilitárias ---
def carregar_dados(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# --- Carrega dados ---
alunos = carregar_dados(arquivo_json)
turmas = carregar_dados(turmas_json)

print("========== EDIÇÃO DE ALUNO ==========\n")

if not alunos:
    print("Nenhum aluno cadastrado.")
    sys.exit(0)

id_alvo = input("Digite o ID do aluno que deseja editar: ").strip()
try:
    id_alvo = int(id_alvo)
except ValueError:
    print("Erro: o ID deve ser um número inteiro.")
    sys.exit(1)

# --- Localiza aluno ---
aluno = next((a for a in alunos if int(a.get("id", -1)) == id_alvo), None)
if aluno is None:
    print("Aluno não encontrado.")
    sys.exit(1)

# --- Descobre nome da turma atual ---
turma_atual_nome = "Não matriculado"
if "turmaId" in aluno and aluno["turmaId"]:
    turma_atual = next((t for t in turmas if int(t["id"]) == int(aluno["turmaId"])), None)
    if turma_atual:
        turma_atual_nome = turma_atual["nome"]

print(f"\nEditando Aluno ID {aluno['id']} - {aluno['nome']}")

# --- Edição de dados ---
novo_nome = input("Novo nome (Enter para manter): ").strip()
novo_email = input("Novo e-mail (Enter para manter): ").strip()
nova_senha = getpass.getpass("Nova senha (Enter para manter): ").strip()

if novo_nome:
    aluno["nome"] = novo_nome
if novo_email:
    aluno["email"] = novo_email
if nova_senha:
    aluno["senha"] = gerar_hash_senha(nova_senha)

# --- Edição de turma ---
if turmas:
    print("\nTurmas disponíveis:")
    for t in turmas:
        print(f"{t['id']}. {t['nome']}")

    if aluno.get("turmaId"):
        trocar = input(f"\nO aluno já está matriculado na turma '{turma_atual_nome}'. Deseja realmente trocar a matrícula? (s/n): ").strip().lower()
    else:
        trocar = input("\nO aluno não está matriculado em nenhuma turma. Deseja matricular agora? (s/n): ").strip().lower()

    if trocar == "s":
        try:
            nova_turma = int(input("Digite o ID da nova turma: ").strip())
            if any(int(t.get("id", -1)) == nova_turma for t in turmas):
                aluno["turmaId"] = nova_turma
                turma_nome = next((t["nome"] for t in turmas if int(t["id"]) == nova_turma), "")
                print(f"Aluno agora matriculado na turma: {turma_nome}")
            else:
                print("Turma não encontrada. Mantendo turma atual.")
        except ValueError:
            print("Entrada inválida. Mantendo turma atual.")
else:
    print("\nNenhuma turma cadastrada. Não é possível alterar a matrícula.")

# --- Salva alterações ---
salvar_dados(arquivo_json, alunos)

print("\nAluno atualizado com sucesso!")
