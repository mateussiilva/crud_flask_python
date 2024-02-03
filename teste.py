
clientes = [
    {"id": 1, "nome": "Mateus jose da silva", "idade": 23},
    {"id": 2, "nome": " jose da silva", "idade": 23},


]


def get_for_id(id):
    nome = None
    for cliente in clientes:
        i = int(cliente.get("id")) if cliente.get("id") is not None else 0
        if i == id:
            nome = cliente["nome"]

    return nome

