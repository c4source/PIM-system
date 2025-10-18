# edit_json_aula.py (corrigido)
import json, sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON nao especificado"); sys.exit(1)
arquivo_json = sys.argv[1]

try:
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    print("Erro: arquivo nao encontrado ou vazio."); sys.exit(1)


print("========== EDIÇÃO DE AULA ==========\n")
id_alvo = input("Digite o ID da aula que deseja editar: ").strip()

aula = None
for item in dados:
    if str(item.get("id")) == id_alvo:
        aula = item
        break

if aula is None:
    print("Aula nao encontrada."); sys.exit(1)

print(f"Editando Aula ID {aula['id']}")
novo_tema = input("Novo tema (Enter para manter): ").strip()
novo_prof = input("Novo ProfessorID (Enter para manter): ").strip()
nova_turma = input("Nova turmaId (Enter para manter): ").strip()

if novo_tema: aula["tema"] = novo_tema
if novo_prof:
    aula["professorId"] = int(novo_prof) 
if nova_turma:
    aula["turmaId"] = int(nova_turma) 

with open(arquivo_json, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)
print("Registro atualizado com sucesso!")
