import json, sys, os

if len(sys.argv) < 3:
    print("Uso: python read_json_aula.py <arquivo> <id_professor>")
    sys.exit(1)

arquivo_json = sys.argv[1]
professor_id = int(sys.argv[2])

with open(arquivo_json, "r", encoding="utf-8") as f:
    aulas = json.load(f)

print("========== LISTA DE AULAS ==========\n")
for a in aulas:
    if professor_id != 0 and int(a.get("professorId", 0)) != professor_id:
        continue
    print(f"ID: {a.get('id')}")
    print(f"Tema: {a.get('tema')}")
    print("-" * 40)
