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

# --- Carregar arquivos ---
atividades = carregar_dados(arquivo_json)
turmas = carregar_dados(turmas_json)
aulas = carregar_dados(aulas_json)
professores = carregar_dados(professores_json)

print("========== EDIÇÃO DE ATIVIDADE ==========\n")

if not atividades:
    print("Nenhuma atividade cadastrada.")
    sys.exit(0)

# --- Escolher atividade ---
id_alvo = input("Digite o ID da atividade que deseja editar: ").strip()
try:
    id_alvo = int(id_alvo)
except ValueError:
    print("Erro: o ID deve ser um número inteiro.")
    sys.exit(1)

atividade = next((a for a in atividades if int(a.get("id", -1)) == id_alvo), None)
if atividade is None:
    print("Atividade não encontrada.")
    sys.exit(1)

# --- Mostrar informações atuais ---
turma_atual = next((t for t in turmas if int(t["id"]) == int(atividade.get("turmaId", -1))), None)
aula_atual = next((a for a in aulas if int(a["id"]) == int(atividade.get("aulaId", -1))), None)
prof_atual = None
if turma_atual and turma_atual.get("professorId"):
    prof_atual = next((p for p in professores if int(p["id"]) == int(turma_atual["professorId"])), None)

print(f"Editando Atividade ID {atividade['id']}")
print(f"Título atual: {atividade.get('titulo', '(sem título)')}")
print(f"Descrição atual: {atividade.get('descricao', '(sem descrição)')}")
print(f"Turma atual: {turma_atual['nome'] if turma_atual else 'Não associada'}")
print(f"Aula atual: {aula_atual['tema'] if aula_atual else 'Não associada'}")
print(f"Professor responsável: {prof_atual['nome'] if prof_atual else 'Não definido'}")

# --- Editar dados básicos ---
novo_titulo = input("Novo título (Enter para manter): ").strip()
nova_desc = input("Nova descrição (Enter para manter): ").strip()

if novo_titulo:
    atividade["titulo"] = novo_titulo
if nova_desc:
    atividade["descricao"] = nova_desc

# --- Permitir alterar turma (e atualizar automaticamente o professor e aulas) ---
print("\nTurmas disponíveis:")
for t in turmas:
    prof_id = t.get("professorId")
    prof_nome = "Sem professor"
    if prof_id:
        prof = next((p for p in professores if int(p["id"]) == int(prof_id)), None)
        if prof:
            prof_nome = prof["nome"]
    print(f"{t['id']}. {t['nome']} - Professor: {prof_nome}")

trocar_turma = input("\nDeseja alterar a turma da atividade? (s/n): ").strip().lower()
if trocar_turma == "s":
    try:
        nova_turma_id = int(input("Digite o ID da nova turma: ").strip())
        nova_turma = next((t for t in turmas if int(t["id"]) == nova_turma_id), None)
        if nova_turma:
            atividade["turmaId"] = nova_turma_id
            atividade["professorId"] = nova_turma.get("professorId", None)
            print(f"Turma alterada para: {nova_turma['nome']}")
            # Atualizar aula se quiser
            aulas_turma = [a for a in aulas if int(a["turmaId"]) == nova_turma_id]
            if aulas_turma:
                print("\nAulas disponíveis dessa turma:")
                for a in aulas_turma:
                    print(f"{a['id']}. {a['tema']}")
                nova_aula_id = input("Digite o ID da nova aula (ou Enter para manter atual): ").strip()
                if nova_aula_id:
                    try:
                        nova_aula_id = int(nova_aula_id)
                        if any(int(a["id"]) == nova_aula_id for a in aulas_turma):
                            atividade["aulaId"] = nova_aula_id
                            print("Aula atualizada com sucesso.")
                        else:
                            print("Aula não encontrada. Mantendo atual.")
                    except ValueError:
                        print("Entrada inválida. Mantendo aula atual.")
            else:
                atividade["aulaId"] = None
                print("Nova turma não possui aulas cadastradas.")
        else:
            print("Turma não encontrada. Mantendo atual.")
    except ValueError:
        print("Entrada inválida. Mantendo turma atual.")

# --- Salvar alterações ---
salvar_dados(arquivo_json, atividades)
print("\nAtividade atualizada com sucesso!")
