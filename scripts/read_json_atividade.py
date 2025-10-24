import json, sys, os

if len(sys.argv) < 4:
    print("Uso: python read_json_atividade.py <arquivo> <id_usuario> <tipo_usuario>")
    sys.exit(1)

arquivo_json = sys.argv[1]
usuario_id = int(sys.argv[2])
tipo_usuario = int(sys.argv[3])

with open(arquivo_json, "r", encoding="utf-8") as f:
    atividades = json.load(f)

print("========== LISTA DE ATIVIDADES ==========\n")
for a in atividades:
    # Se for professor, filtra pelo professorId
    if tipo_usuario == 2 and int(a.get("professorId", 0)) != usuario_id:
        continue
    # Se for aluno, mostra apenas atividades da turma do aluno
    # (pode melhorar mais tarde com vínculo direto)
    print(f"ID: {a.get('id')}")
    print(f"Título: {a.get('titulo')}")
    print(f"Descrição: {a.get('descricao')}")
    print("-" * 40)
