import json
import sys
import os

NOTAS_JSON = "data/notas.json"
ALUNOS_JSON = "data/alunos.json"
ATIVIDADES_JSON = "data/atividades.json"
TURMAS_JSON = "data/turmas.json"

# --- Funções auxiliares ---
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

# --- Carregar dados ---
notas = carregar_dados(NOTAS_JSON)
alunos = carregar_dados(ALUNOS_JSON)
atividades = carregar_dados(ATIVIDADES_JSON)
turmas = carregar_dados(TURMAS_JSON)

print("========== LANÇAMENTO DE NOTA ==========\n")

if not alunos or not atividades:
    print("⚠️ É necessário ter alunos e atividades cadastradas antes de lançar notas.")
    sys.exit(0)

# --- Selecionar aluno ---
print("Alunos disponíveis:")
for a in alunos:
    print(f"{a['id']}. {a['nome']}")
try:
    aluno_id = int(input("\nDigite o ID do aluno: ").strip())
except ValueError:
    print("ID inválido.")
    sys.exit(1)
aluno = next((a for a in alunos if int(a["id"]) == aluno_id), None)
if not aluno:
    print("Aluno não encontrado.")
    sys.exit(1)

# --- Selecionar atividade ---
print("\nAtividades disponíveis:")
for at in atividades:
    print(f"{at['id']}. {at['titulo']}")
try:
    atividade_id = int(input("\nDigite o ID da atividade: ").strip())
except ValueError:
    print("ID inválido.")
    sys.exit(1)
atividade = next((at for at in atividades if int(at["id"]) == atividade_id), None)
if not atividade:
    print("Atividade não encontrada.")
    sys.exit(1)

# --- Lançar nota ---
try:
    nota = float(input("Digite a nota (0 a 10): ").strip())
except ValueError:
    nota = 0.0
status = input("Digite o status (pendente, entregue, corrigida): ").strip().lower() or "pendente"

# --- Salvar ---
novo = {
    "id": proximo_id(notas),
    "alunoId": aluno_id,
    "atividadeId": atividade_id,
    "nota": nota,
    "status": status
}
notas.append(novo)
salvar_dados(NOTAS_JSON, notas)

print("\n✅ Nota lançada com sucesso!")
print(f"Aluno: {aluno['nome']}")
print(f"Atividade: {atividade['titulo']}")
print(f"Nota: {nota} | Status: {status}")
