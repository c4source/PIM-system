import sys, json, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data")

ADM   = os.path.join(DATA, "administradores.json")
PROF  = os.path.join(DATA, "professores.json")
ALUNO = os.path.join(DATA, "alunos.json")


#Abre um arquivo JSON e carrega seus dados (Transforma o conteudo em uma lista Python)
#Retorna uma lista vazia se o arquivo não existir. 

def load(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f: 
            return json.load(f)
    except json.JSONDecodeError: 
        return []

def find_user(usuario,senha):
    for u in load(ADM):
        if u.get("login") == usuario and u.get("senha") == senha:
            return 1 
    for u in load(PROF):
        if u.get("login") == usuario and u.get("senha") == senha:
            return 2
    for u in load(ALUNO):
        if u.get("login") == usuario and u.get("senha") == senha:
            return 3 
    return 0
    
def main():
    if len(sys.argv) < 3:
        print("0")
        return 
    
    login, senha = sys.argv[1], sys.argv[2]
    print(find_user(login, senha))


if __name__ == "__main__":
    main()   