from typing import List


class Pedido:

    def __init__(
        self,
        codigo: int,
        cpf: str,
        produtos: List[str]
    ):
        self.codigo = codigo
        self.cpf = cpf
        self.produtos = produtos

        self.esta_entregue = False
        self.esta_cancelado = False
        self.prioritario = False
        self.observacao = ""

    def cancelar(self) -> bool:

        if self.esta_entregue:
            return False

        if self.esta_cancelado:
            return False

        self.esta_cancelado = True
        return True

    def adicionar_observacao(
        self,
        observacao: str
    ) -> bool:

        if self.esta_entregue:
            return False

        observacao = observacao.strip()

        if not observacao:
            return False

        if len(observacao) > 200:
            return False

        self.observacao = observacao
        return True

    def tornar_prioritario(self) -> bool:

        if self.esta_cancelado:
            return False

        if self.esta_entregue:
            return False

        self.prioritario = True
        return True
