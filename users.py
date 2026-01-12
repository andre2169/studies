
# Eu tenho uma lista de usuários guardada na memória do programa.
# Quero filtrar os usuários ativos e inativos.

# lista chamada users com vários usuários dentro, cada usuário é um dicionário, ou seja: “Um conjunto de chave → valor”.
users = [
    {"name": "Andre", "email": "andre@example.com", "password": "123", "active": True},
    {"name": "Darlei", "email": "darlei@example.com", "password": "123", "active": True},
    {"name": "Lari", "email": "lari@example.com", "password": "123", "active": False},
    {"name": "Isabel", "email": "isabel@example.com", "password": "123", "active": False},
    {"name": "Maria", "email": "maria@example.com", "password": "123", "active": True},
    {"name": "Pedro", "email": "pedro@example.com", "password": "123", "active": False},
    {"name": "João", "email": "joao@example.com", "password": "123", "active": True},
]

# Crio uma função que recebe um parâmetro dizendo qual tipo de usuário quero.
def filter_users(is_active):
  # Crio uma lista vazia para guardar o resultado.
    filtered_users = []
# Percorro a lista de usuários.
    for user in users:
        # Verifico se o usuário é do tipo que quero.
        if user["active"] is is_active:
            # Adiciono o usuário no final da lista de resultado.
            filtered_users.append(user)
# Retorno a lista de resultado.
    return filtered_users

# Testando a função.
print(filter_users(True))
print(filter_users(False))


# Terminal c:\> Python users.py
#Saída esperada:

# [{'name': 'Andre', 'email': 'andre@example.com', 'password': '123', 'active': True}, 
#  {'name': 'Darlei', 'email': 'darlei@example.com', 'password': '123', 'active': True},
#  {'name': 'Maria', 'email': 'maria@example.com', 'password': '123', 'active': True},
#  {'name': 'João', 'email': 'joao@example.com', 'password': '123', 'active': True}]

# [{'name': 'Lari', 'email': 'lari@example.com', 'password': '123', 'active': False},
#  {'name': 'Isabel', 'email': 'isabel@example.com', 'password': '123', 'active': False},
#  {'name': 'Pedro', 'email': 'pedro@example.com', 'password': '123', 'active': False}]