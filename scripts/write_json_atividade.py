import json
import sys
import os

if len(sys.argv) < 2:
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]
turmas_json = os.path.join(os.path.dirname(arquivo_json), "turmas.json")
aulas_json = os.path.join(os.path.dirname(arquivo_json), "aulas.json")
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

# --- Carrega dados ---
atividades = carregar_dados(arquivo_json)
turmas = carregar_dados(turmas_json)
aulas = carregar_dados(aulas_json)
professores = carregar_dados(professores_json)

print("========== CADASTRO DE ATIVIDADE ==========\n")

if not turmas:
    print("⚠️ Nenhuma turma cadastrada. Cadastre uma turma antes de criar atividades.")
    sys.exit(0)

# --- Listar turmas e professores ---
print("Turmas disponíveis:\n")
for t in turmas:
    prof_id = t.get("professorId")
    prof_nome = "Sem professor"
    if prof_id:
        prof = next((p for p in professores if int(p["id"]) == int(prof_id)), None)
        if prof:
            prof_nome = prof["nome"]
    print(f"{t['id']}. {t['nome']} - Professor: {prof_nome}")

# --- Escolher turma ---
try:
    turma_id = int(input("\nDigite o ID da turma para associar à atividade: ").strip())
except ValueError:
    print("Erro: o ID deve ser numérico.")
    sys.exit(1)

turma = next((t for t in turmas if int(t["id"]) == turma_id), None)
if not turma:
    print("Turma não encontrada.")
    sys.exit(1)

# --- Listar aulas da turma selecionada ---
aulas_turma = [a for a in aulas if int(a.get("turmaId", -1)) == turma_id]
if not aulas_turma:
    print("\n⚠️ Nenhuma aula cadastrada para essa turma.")
    aula_id = None
else:
    print("\nAulas disponíveis dessa turma:")
    for a in aulas_turma:
        print(f"{a['id']}. {a['tema']}")
    try:
        aula_id = int(input("\nDigite o ID da aula relacionada (ou 0 para nenhuma): ").strip())
        if aula_id == 0 or not any(int(a["id"]) == aula_id for a in aulas_turma):
            aula_id = None
    except ValueError:
        aula_id = None

# --- Professor responsável (herdado da turma) ---
professor_id = turma.get("professorId")

# --- Cadastrar atividade ---
nova = {}
nova["id"] = proximo_id(atividades)
nova["titulo"] = input("Título da atividade: ").strip()
nova["descricao"] = input("Descrição: ").strip()
nova["turmaId"] = turma_id
nova["aulaId"] = aula_id
nova["professorId"] = professor_id

atividades.append(nova)
salvar_dados(arquivo_json, atividades)

print("\nAtividade cadastrada com sucesso!")
print(f"ID: {nova['id']}")
print(f"Turma: {turma['nome']}")
if aula_id:
    aula_nome = next((a["tema"] for a in aulas if int(a["id"]) == aula_id), "(sem tema)")
    print(f"Aula: {aula_nome}")
if professor_id:
    prof_nome = next((p["nome"] for p in professores if int(p["id"]) == int(professor_id)), "Desconhecido")
    print(f"Professor responsável: {prof_nome}")
