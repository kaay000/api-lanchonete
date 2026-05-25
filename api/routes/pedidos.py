from fastapi import APIRouter

from schemas.pedido import (
    ObservacaoInput,
    PedidoFilaOut
)

from services.lanchonete_service import (
    LanchoneteService
)

from repositories.pedido_repository import PedidoRepository


router = APIRouter()

repository = PedidoRepository()

service = LanchoneteService(repository)


@router.post(
    "/lanchonete/pedidos/{cod_pedido}/observacao"
)
def adicionar_observacao(
    cod_pedido: int,
    dados: ObservacaoInput
):

    return service.adicionar_observacao(
        cod_pedido,
        dados.observacao
    )


@router.post(
    "/lanchonete/pedidos/{cod_pedido}/cancelar"
)
def cancelar_pedido(
    cod_pedido: int
):

    return service.cancelar_pedido(
        cod_pedido
    )


@router.post(
    "/lanchonete/pedidos/{cod_pedido}/prioridade"
)
def tornar_prioritario(
    cod_pedido: int
):

    return service.tornar_pedido_prioritario(
        cod_pedido
    )


@router.get(
    "/lanchonete/pedidos/fila/preparo",
    response_model=list[PedidoFilaOut]
)
def listar_fila():

    return service.listar_fila_preparo()
