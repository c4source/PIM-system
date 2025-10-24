import json, sys

if len(sys.argv) < 3:
    print("Uso: python read_json_nota.py <arquivo> <id_aluno>")
    sys.exit(1)

arquivo_json = sys.argv[1]
aluno_id = int(sys.argv[2])

with open(arquivo_json, "r", encoding="utf-8") as f:
    notas = json.load(f)

print("========== MINHAS NOTAS ==========\n")
for n in notas:
    if int(n.get("alunoId", 0)) != aluno_id:
        continue
    print(f"Atividade ID: {n['atividadeId']}")
    print(f"Nota: {n['nota']} ({n['status']})")
    print("-" * 40)
