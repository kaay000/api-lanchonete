from domain.pedido import Pedido

from repositories.pedido_repository import (
    PedidoRepository
)

from services.lanchonete_service import (
    LanchoneteService
)


def test_deve_cancelar_pedido():

    pedido = Pedido(
        1,
        "123",
        ["X-Burger"]
    )

    resultado = pedido.cancelar()

    assert resultado is True
    assert pedido.esta_cancelado is True


def test_nao_deve_cancelar_pedido_entregue():

    pedido = Pedido(
        1,
        "123",
        ["X-Burger"]
    )

    pedido.esta_entregue = True

    resultado = pedido.cancelar()

    assert resultado is False


def test_deve_adicionar_observacao():

    pedido = Pedido(
        1,
        "123",
        ["X-Burger"]
    )

    resultado = pedido.adicionar_observacao(
        "Sem cebola"
    )

    assert resultado is True
    assert pedido.observacao == "Sem cebola"


def test_nao_deve_aceitar_observacao_vazia():

    pedido = Pedido(
        1,
        "123",
        ["X-Burger"]
    )

    resultado = pedido.adicionar_observacao(
        ""
    )

    assert resultado is False


def test_deve_tornar_pedido_prioritario():

    pedido = Pedido(
        1,
        "123",
        ["X-Burger"]
    )

    resultado = pedido.tornar_prioritario()

    assert resultado is True
    assert pedido.prioritario is True


def test_fila_deve_ter_prioritarios_primeiro():

    repository = PedidoRepository()

    pedido1 = Pedido(1, "111", ["X"])
    pedido2 = Pedido(2, "222", ["Y"])

    pedido2.tornar_prioritario()

    repository.adicionar(pedido1)
    repository.adicionar(pedido2)

    service = LanchoneteService(repository)

    fila = service.listar_fila_preparo()

    assert fila[0].codigo == 2


def test_fila_nao_deve_listar_cancelados():

    repository = PedidoRepository()

    pedido1 = Pedido(1, "111", ["X"])
    pedido2 = Pedido(2, "222", ["Y"])

    pedido2.cancelar()

    repository.adicionar(pedido1)
    repository.adicionar(pedido2)

    service = LanchoneteService(repository)

    fila = service.listar_fila_preparo()

    assert len(fila) == 1
    assert fila[0].codigo == 1
