# edit_json_turma.py (corrigido)
import json, sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON nao especificado"); sys.exit(1)
arquivo_json = sys.argv[1]

try:
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    print("Erro: arquivo nao encontrado ou vazio."); sys.exit(1)

print("========== EDIÇÃO DE TURMA ==========\n")
id_alvo = input("Digite o ID da turma que deseja editar: ").strip()

turma = None
for item in dados:
    if str(item.get("id")) == id_alvo:
        turma = item
        break

if turma is None:
    print("Turma nao encontrada."); sys.exit(1)

print(f"Editando Turma ID {turma['id']} - {turma.get('nome','(sem nome)')}")
novo_nome = input("Novo nome (Enter para manter): ").strip()
if novo_nome: turma["nome"] = novo_nome

with open(arquivo_json, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)
print("Registro atualizado com sucesso!")
