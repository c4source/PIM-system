# scripts/validar_login.py
import sys, json, os, hashlib, getpass 

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(BASE, "..", "data"))

ADM   = os.path.join(DATA, "administradores.json")
PROF  = os.path.join(DATA, "professores.json")
ALUNO = os.path.join(DATA, "alunos.json")

def load(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

# scripts/validar_login.py
import sys, json, os, hashlib, getpass

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(BASE, "..", "data"))

ADM   = os.path.join(DATA, "administradores.json")
PROF  = os.path.join(DATA, "professores.json")
ALUNO = os.path.join(DATA, "alunos.json")

def load(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

def gerar_hash_senha(senha):
    """ 
    Gera um hash SHA-256 para a senha
    """
    return hashlib.sha256(senha.encode()).hexdigest()

def same_email(a, b):
    return (a or "").strip().lower() == (b or "").strip().lower()

def same_senha(senha_armazenada, senha_digitada):
    """ Compara o hash da senha digitada com o hash armazenado """
    return senha_armazenada == gerar_hash_senha(senha_digitada)

def find_user(email, senha):
    # 1 = admin, 2 = professor, 3 = aluno, 0 = não achou
    for u in load(ADM):
        if same_email(u.get("email"), email) and same_senha(u.get("senha"), senha):
            print(f"1|{u.get('id', 0)}|{u.get('nome', 'Administrador')}")
            return
    for u in load(PROF):
        if same_email(u.get("email"), email) and same_senha(u.get("senha"), senha):
            print(f"2|{u.get('id', 0)}|{u.get('nome', 'Professor')}")
            return
    for u in load(ALUNO):
        if same_email(u.get("email"), email) and same_senha(u.get("senha"), senha):
            print(f"3|{u.get('id', 0)}|{u.get('nome', 'Aluno')}")
            return
    print("0|0|")  # login inválido

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("0|0|")
    else:
        find_user(sys.argv[1], sys.argv[2])

