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
    
    Args:
        senha (str): A senha em texto puro do aluno.
    
    Returns: 
        str: O hash SHA-256 da senha     
    
    """
    return hashlib.sha256(senha.encode()).hexdigest()



def same_email(a, b):
    return (a or "").strip().lower() == (b or "").strip().lower()

def same_senha(senha_armazenada, senha_digitada):
    """
    Compara o hash da senha digitada com o hash armazenado.

    Args:
        senha_armazenada (str): O hash da senha armazenada.
        senha_digitada (str): A senha digitada em texto puro.

    Returns:
        bool: True se os hashes concidierem, e False caso contrário. 

    """
    return senha_armazenada == gerar_hash_senha(senha_digitada)
    


def find_user(email, senha):
    # 1 = admin, 2 = professor, 3 = aluno, 0 = não achou
    for u in load(ADM):
        if same_email(u.get("email"), email) and same_senha(u.get("senha"), senha):
            return 1
    for u in load(PROF):
        if same_email(u.get("email"), email) and same_senha(u.get("senha"), senha):
            return 2
    for u in load(ALUNO):
        if same_email(u.get("email"), email) and same_senha(u.get("senha"), senha):
            return 3
    return 0

def main():
    if len(sys.argv) < 3:
        print("0")
        return
    email, senha = sys.argv[1], sys.argv[2]
    print(find_user(email, senha))

if __name__ == "__main__":
    main()
