import json
import sys
import os

if len(sys.argv) < 2:
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]
turmas_json = os.path.join(os.path.dirname(arquivo_json), "turmas.json")
professores_json = os.path.join(os.path.dirname(arquivo_json), "professores.json")

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

# --- Carrega os arquivos ---
aulas = carregar_dados(arquivo_json)
turmas = carregar_dados(turmas_json)
professores = carregar_dados(professores_json)

print("========== CADASTRO DE AULA ==========\n")

if not turmas:
    print("⚠️ Nenhuma turma cadastrada. Cadastre uma turma antes de criar aulas.")
    sys.exit(0)

# --- Lista turmas e professores ---
print("Turmas disponíveis:\n")
for t in turmas:
    prof_id = t.get("professorId")
    prof_nome = "Sem professor"
    if prof_id:
        prof = next((p for p in professores if int(p["id"]) == int(prof_id)), None)
        if prof:
            prof_nome = prof["nome"]
    print(f"{t['id']}. {t['nome']} - Professor: {prof_nome}")

# --- Escolha da turma ---
try:
    turma_id = int(input("\nDigite o ID da turma para associar à aula: ").strip())
except ValueError:
    print("Entrada inválida. O ID deve ser numérico.")
    sys.exit(1)

turma = next((t for t in turmas if int(t["id"]) == turma_id), None)
if not turma:
    print("Turma não encontrada.")
    sys.exit(1)

professor_id = turma.get("professorId")

# --- Criação da aula ---
nova = {}
nova["id"] = proximo_id(aulas)
nova["turmaId"] = turma_id
nova["professorId"] = professor_id
nova["tema"] = input("Digite o tema da aula: ").strip()

aulas.append(nova)
salvar_dados(arquivo_json, aulas)

print("\nAula cadastrada com sucesso!")
print(f"ID: {nova['id']}")
print(f"Turma: {turma['nome']}")
if professor_id:
    prof_nome = next((p["nome"] for p in professores if int(p["id"]) == int(professor_id)), "Desconhecido")
    print(f"Professor responsável: {prof_nome}")
else:
    print("Professor responsável: não definido")
