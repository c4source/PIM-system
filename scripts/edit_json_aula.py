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

# --- Carrega dados ---
aulas = carregar_dados(arquivo_json)
turmas = carregar_dados(turmas_json)
professores = carregar_dados(professores_json)

print("========== EDIÇÃO DE AULA ==========\n")

if not aulas:
    print("Nenhuma aula cadastrada.")
    sys.exit(0)

# --- Seleciona a aula ---
id_alvo = input("Digite o ID da aula que deseja editar: ").strip()
try:
    id_alvo = int(id_alvo)
except ValueError:
    print("Erro: o ID deve ser um número inteiro.")
    sys.exit(1)

aula = next((a for a in aulas if int(a.get("id", -1)) == id_alvo), None)
if aula is None:
    print("Aula não encontrada.")
    sys.exit(1)

# --- Mostra informações atuais ---
turma_atual = next((t for t in turmas if int(t["id"]) == int(aula.get("turmaId", -1))), None)
prof_atual = None
if turma_atual:
    prof_id = turma_atual.get("professorId")
    prof_atual = next((p for p in professores if int(p["id"]) == int(prof_id)), None)

print(f"Editando Aula ID {aula['id']}")
print(f"Tema atual: {aula.get('tema', '(sem tema)')}")
print(f"Turma atual: {turma_atual['nome'] if turma_atual else 'Não associada'}")
print(f"Professor responsável: {prof_atual['nome'] if prof_atual else 'Não definido'}\n")

# --- Editar tema ---
novo_tema = input("Novo tema (Enter para manter): ").strip()
if novo_tema:
    aula["tema"] = novo_tema

# --- Editar turma (com atualização automática do professor) ---
if turmas:
    print("\nTurmas disponíveis:")
    for t in turmas:
        prof_id = t.get("professorId")
        prof_nome = "Sem professor"
        if prof_id:
            prof = next((p for p in professores if int(p["id"]) == int(prof_id)), None)
            if prof:
                prof_nome = prof["nome"]
        print(f"{t['id']}. {t['nome']} - Professor: {prof_nome}")

    trocar = input("\nDeseja alterar a turma desta aula? (s/n): ").strip().lower()
    if trocar == "s":
        try:
            nova_turma_id = int(input("Digite o ID da nova turma: ").strip())
            nova_turma = next((t for t in turmas if int(t["id"]) == nova_turma_id), None)
            if nova_turma:
                aula["turmaId"] = nova_turma_id
                aula["professorId"] = nova_turma.get("professorId", None)
                print(f"Aula agora associada à turma: {nova_turma['nome']}")
                if nova_turma.get("professorId"):
                    prof_nome = next((p["nome"] for p in professores if int(p["id"]) == int(nova_turma["professorId"])), "")
                    print(f"Professor responsável atualizado para: {prof_nome}")
                else:
                    print("Nova turma não possui professor definido.")
            else:
                print("Turma não encontrada. Mantendo turma atual.")
        except ValueError:
            print("Entrada inválida. Mantendo turma atual.")
else:
    print("Nenhuma turma cadastrada. Não é possível alterar a turma.")

# --- Salva alterações ---
salvar_dados(arquivo_json, aulas)
print("\nAula atualizada com sucesso!")
