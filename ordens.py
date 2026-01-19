# Tenho uma lista de pedidos (orders) guardada na memória.
# Quero criar uma função que retorne pedidos pagos e nao pagos. 

orders = [
    {"id": 1, "customer": "Andre", "total": 150.0, "paid": True},
    {"id": 2, "customer": "Lari", "total": 89.9, "paid": False},
    {"id": 3, "customer": "Maria", "total": 230.0, "paid": True},
    {"id": 4, "customer": "João", "total": 50.0, "paid": False},
]

# Função para retornar pedidos pagos ou não pagos
def get_paid_orders(is_paid):
    paid_orders = []
# Itera sobre a lista de pedidos e filtra os pagos
    for order in orders:
        # Verifica se o pedido está pago
        if order["paid"] == is_paid:
            # Adiciona o pedido pago à lista
            paid_orders.append(order)
            # Imprime mensagem dependendo se é pago ou não
            if is_paid:
                print("Pedido pago encontrado:", order["id"])
            else:
                print("Pedido não pago encontrado:", order["id"])
# Retorna a lista de pedidos pagos ou não pagos
    return paid_orders

# Testando a função
print(get_paid_orders(True))
print(get_paid_orders(False))


# Terminal c:\ordens> Python ordens.py
# Saida esperada:

# Pedido pago encontrado: 1
# Pedido pago encontrado: 3
# [{'id': 1, 'customer': 'Andre', 'total': 150.0, 'paid': True}, {'id': 3, 'customer': 'Maria', 'total': 230.0, 'paid': True}]

# Pedido não pago encontrado: 2
# Pedido não pago encontrado: 4
#[{'id': 2, 'customer': 'Lari', 'total': 89.9, 'paid': False}, {'id': 4, 'customer': 'João', 'total': 50.0, 'paid': False}]