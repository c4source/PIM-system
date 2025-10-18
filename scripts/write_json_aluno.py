import json
import sys
import os

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

def proximo_id(lista):
    return (max(int(x.get("id", 0)) for x in lista) + 1) if lista else 1

# --- Carrega dados existentes ---
alunos = carregar_dados(arquivo_json)
turmas = carregar_dados(turmas_json)

print("========== CADASTRO DE ALUNO ==========\n")

novo = {}
novo["id"] = proximo_id(alunos)
novo["nome"] = input("Digite o nome do aluno: ").strip()
novo["email"] = input("Digite o e-mail: ").strip()
novo["senha"] = input("Crie uma senha: ").strip()

# --- Seleção de turma ---
if not turmas:
    print("\n⚠️ Nenhuma turma cadastrada. Cadastre uma turma antes de associar o aluno.")
    novo["turmaId"] = None
else:
    print("\nTurmas disponíveis:")
    for t in turmas:
        print(f"{t['id']}. {t['nome']}")
    try:
        turma_id = int(input("Digite o ID da turma para matricular o aluno: ").strip())
        if not any(int(t.get("id", -1)) == turma_id for t in turmas):
            print("Turma não encontrada. O aluno será cadastrado sem turma.")
            novo["turmaId"] = None
        else:
            novo["turmaId"] = turma_id
    except ValueError:
        print("Entrada inválida. O aluno será cadastrado sem turma.")
        novo["turmaId"] = None

# --- Salva ---
alunos.append(novo)
salvar_dados(arquivo_json, alunos)

print(f"\nAluno cadastrado com sucesso!")
if novo["turmaId"]:
    turma_nome = next((t['nome'] for t in turmas if int(t['id']) == novo["turmaId"]), None)
    print(f"Aluno matriculado na turma: {turma_nome}")
else:
    print("Aluno cadastrado sem turma associada.")
