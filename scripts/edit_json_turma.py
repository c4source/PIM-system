import json
import sys
import os

if len(sys.argv) < 2:
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]
professores_json = os.path.join(os.path.dirname(arquivo_json), "professores.json")

def carregar_dados(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

turmas = carregar_dados(arquivo_json)
professores = carregar_dados(professores_json)

print("========== EDIÇÃO DE TURMA ==========\n")

if not turmas:
    print("Nenhuma turma cadastrada.")
    sys.exit(0)

id_alvo = input("Digite o ID da turma que deseja editar: ").strip()
try:
    id_alvo = int(id_alvo)
except ValueError:
    print("Erro: o ID deve ser um número inteiro.")
    sys.exit(1)

turma = next((t for t in turmas if int(t.get("id", -1)) == id_alvo), None)
if turma is None:
    print("Turma não encontrada.")
    sys.exit(1)

prof_atual = None
if turma.get("professorId"):
    prof_atual = next((p for p in professores if int(p["id"]) == turma["professorId"]), None)

print(f"\nEditando Turma ID {turma['id']} - {turma['nome']}")
print(f"Professor atual: {prof_atual['nome'] if prof_atual else 'Nenhum'}")

novo_nome = input("Novo nome (Enter para manter): ").strip()
if novo_nome:
    turma["nome"] = novo_nome

# Troca de professor
if professores:
    print("\nProfessores disponíveis:")
    for p in professores:
        print(f"{p['id']}. {p['nome']}")
    trocar = input("Deseja alterar o professor responsável? (s/n): ").strip().lower()
    if trocar == "s":
        try:
            novo_prof = int(input("Digite o ID do novo professor: ").strip())
            if any(int(p.get("id", -1)) == novo_prof for p in professores):
                turma["professorId"] = novo_prof
                prof_nome = next((p["nome"] for p in professores if int(p["id"]) == novo_prof), "")
                print(f"Professor alterado para: {prof_nome}")
            else:
                print("Professor não encontrado. Mantendo o atual.")
        except ValueError:
            print("Entrada inválida. Mantendo o professor atual.")
else:
    print("Nenhum professor cadastrado. Não é possível alterar o professor da turma.")

salvar_dados(arquivo_json, turmas)
print("\nTurma atualizada com sucesso!")
