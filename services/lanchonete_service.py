from fastapi import HTTPException

from repositories.pedido_repository import PedidoRepository


class LanchoneteService:

    def __init__(
        self,
        repository: PedidoRepository
    ):
        self.repository = repository

    def cancelar_pedido(
        self,
        cod_pedido: int
    ):

        pedido = self.repository.buscar_por_codigo(
            cod_pedido
        )

        if not pedido:
            raise HTTPException(
                status_code=404,
                detail="Pedido não encontrado"
            )

        if not pedido.cancelar():
            raise HTTPException(
                status_code=400,
                detail="Pedido não pode ser cancelado"
            )

        return {
            "mensagem": "Pedido cancelado"
        }

    def adicionar_observacao(
        self,
        cod_pedido: int,
        observacao: str
    ):

        pedido = self.repository.buscar_por_codigo(
            cod_pedido
        )

        if not pedido:
            raise HTTPException(
                status_code=404,
                detail="Pedido não encontrado"
            )

        if not pedido.adicionar_observacao(
            observacao
        ):
            raise HTTPException(
                status_code=400,
                detail="Observação inválida"
            )

        return {
            "mensagem": "Observação adicionada"
        }

    def tornar_pedido_prioritario(
        self,
        cod_pedido: int
    ):

        pedido = self.repository.buscar_por_codigo(
            cod_pedido
        )

        if not pedido:
            raise HTTPException(
                status_code=404,
                detail="Pedido não encontrado"
            )

        if not pedido.tornar_prioritario():
            raise HTTPException(
                status_code=400,
                detail="Pedido não pode virar prioritário"
            )

        return {
            "mensagem": "Pedido prioritário"
        }

    def listar_fila_preparo(self):

        pedidos = self.repository.listar()

        ativos = [
            pedido
            for pedido in pedidos
            if not pedido.esta_cancelado
            and not pedido.esta_entregue
        ]

        prioritarios = [
            pedido
            for pedido in ativos
            if pedido.prioritario
        ]

        normais = [
            pedido
            for pedido in ativos
            if not pedido.prioritario
        ]

        return prioritarios + normais
