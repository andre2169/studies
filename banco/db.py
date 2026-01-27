# banco/db.py
import sqlite3

# Criação do banco de dados e da tabela contas_bancarias
conexao = sqlite3.connect('banco.db')
# Criação do cursor
cursor = conexao.cursor()


# Criação da tabela contas_bancarias
cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    saldo REAL NOT NULL,
    cpf TEXT NOT NULL UNIQUE
               )""")

# Inserção de dados iniciais na tabela contas_bancarias
# Verifica se a tabela já possui dados
# Se não houver dados, insere os registros iniciais
# Verifica a quantidade de registros na tabela
cursor.execute("SELECT COUNT(*) FROM contas_bancarias")
quantidade = cursor.fetchone()[0]

if quantidade == 0:
    cursor.execute("""INSERT INTO contas_bancarias (titular, saldo, cpf) VALUES
               ('João Silva', 1500.00, '123.456.789-00'),
               ('Maria Oliveira', 2500.50, '987.654.321-00  '),
               ('Carlos Souza', 300.75, '456.789.123-00'),
               ('Ana Pereira', 1200.00, '321.654.987-00'),
               ('Pedro Lima', 5000.00, '654.321.987-00'),
               ('Juliana Fernandes', 750.25, '789.123.456-00'),
               ('Lucas Almeida', 1800.00, '159.753.486-00'),
               ('Mariana Costa', 2200.40, '357.159.258-00'),
               ('Rafael Gomes', 950.60, '951.753.852-00'),
               ('Beatriz Rocha', 4000.00, '258.456.789-00')
               """)


# Atualiza o saldo de uma conta para um valor negativo
cursor.execute("""UPDATE contas_bancarias
                SET saldo = -5000
                WHERE id = 2""")

# Consulta para verificar os dados após a atualização
cursor.execute("SELECT * FROM contas_bancarias")
contas = cursor.fetchall()

for conta in contas:
    id, titular, saldo, cpf = conta
    print(f"""ID: {id}, 
Titular: {titular},
Saldo: {saldo},
CPF: {cpf}""")
    print("\n")

# Confirma as alterações
conexao.commit()
# Fechamento da conexão
conexao.close()
print("OK, Sucesso.")