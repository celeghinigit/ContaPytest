# ContaPoupanca.py
from ContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    """Conta bancária que permite aplicar juros sobre o saldo atual."""

    def render_juros(self, taxa: float) -> float:
        """Aplica a taxa percentual (em formato decimal) ao saldo."""
        self._saldo += self._saldo * taxa
        return self._saldo
