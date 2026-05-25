from domain.pedido import Pedido


class PedidoRepository:

    def __init__(self):
        self.pedidos = []

    def adicionar(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def buscar_por_codigo(
        self,
        codigo: int
    ):

        for pedido in self.pedidos:

            if pedido.codigo == codigo:
                return pedido

        return None

    def listar(self):
        return self.pedidos
