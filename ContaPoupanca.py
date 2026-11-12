# ContaPoupanca.py
from ContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    """Herda de ContaBancaria e adiciona funcionalidade de rendimento."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        super().__init__(titular, saldo_inicial)

    def render_juros(self, taxa: float) -> float:
        """Aplica a taxa de juros ao saldo e retorna o saldo atualizado."""
        if taxa < 0:
            raise ValueError("A taxa de juros não pode ser negativa.")
        self._saldo += self._saldo * taxa
        return self._saldo
