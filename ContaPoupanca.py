# ContaPoupanca.py
from ContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    """Conta bancária que permite aplicar rendimento sobre o saldo."""

    def render_juros(self, taxa: float) -> float:
        if taxa < 0:
            raise ValueError("A taxa de juros não pode ser negativa.")
        self._saldo += self._saldo * taxa
        return self._saldo
