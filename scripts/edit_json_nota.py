import json
import sys
import os

NOTAS_JSON = "data/notas.json"
ALUNOS_JSON = "data/alunos.json"
ATIVIDADES_JSON = "data/atividades.json"

def carregar_dados(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

notas = carregar_dados(NOTAS_JSON)
alunos = carregar_dados(ALUNOS_JSON)
atividades = carregar_dados(ATIVIDADES_JSON)

print("========== EDIÇÃO DE NOTA ==========\n")

if not notas:
    print("Nenhuma nota cadastrada.")
    sys.exit(0)

# Listar todas as notas
for n in notas:
    aluno_nome = next((a["nome"] for a in alunos if int(a["id"]) == int(n["alunoId"])), "Desconhecido")
    atividade_titulo = next((a["titulo"] for a in atividades if int(a["id"]) == int(n["atividadeId"])), "Desconhecida")
    print(f"{n['id']}. {aluno_nome} - {atividade_titulo} (Nota: {n['nota']}, Status: {n['status']})")

# Selecionar nota
try:
    id_alvo = int(input("\nDigite o ID do registro que deseja editar: ").strip())
except ValueError:
    print("ID inválido.")
    sys.exit(1)

nota = next((n for n in notas if int(n["id"]) == id_alvo), None)
if not nota:
    print("Registro não encontrado.")
    sys.exit(1)

# Editar
nova_nota = input("Nova nota (Enter para manter): ").strip()
novo_status = input("Novo status (pendente, entregue, corrigida - Enter para manter): ").strip().lower()

if nova_nota:
    try:
        nota["nota"] = float(nova_nota)
    except ValueError:
        print("Nota inválida. Mantendo valor anterior.")
if novo_status:
    nota["status"] = novo_status

salvar_dados(NOTAS_JSON, notas)
print("\n✅ Registro atualizado com sucesso!")
