# ContaPoupanca.py
from ContaBancaria import ContaBancaria
class ContaPoupanca(ContaBancaria):
    """Herda de ContaBancaria e adiciona funcionalidade de rendimento."""

    def render_juros(self, taxa: float) -> float:
        rendimento = self._saldo * taxa
        self._saldo += rendimento
        return self._saldo