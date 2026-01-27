# Módulo para geração de tokens seguros, Gera valores aleatórios.
import secrets
# Módulo para hashing de senhas, Usada para transformar texto em hash.
import hashlib


# Banco de dados simulado em memória, dicionário vazio
usuarios = {}
tokens_validos = {}

# 1️⃣ Criar usuário
def criar_usuario(username, senha):
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    usuarios[username] = hash_senha
    print("Usuário criado com sucesso")


# 2️⃣ Login
def login(username, senha):
    if username not in usuarios:
        print("Usuário não existe")
        return None

    hash_digitado = hashlib.sha256(senha.encode()).hexdigest()

    if hash_digitado == usuarios[username]:
        token = secrets.token_hex(16)
        tokens_validos[token] = username
        print("Login realizado com sucesso")
        return token
    else:
        print("Senha incorreta")
        return None
    
    # 3️⃣ Validar token
def validar_token(token):
    if token in tokens_validos:
        return True
    return False


# 4️⃣ Área protegida
def area_protegida(token):
    if validar_token(token):
        usuario = tokens_validos[token]
        print(f"Acesso liberado! Bem-vindo, {usuario}")
    else:
        print("Acesso negado. Token inválido")


# Exemplo de uso
criar_usuario("andre", "1234")

token = login("andre", "1234")

area_protegida(token)
