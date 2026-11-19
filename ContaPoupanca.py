# ContaPoupanca.py
from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    """Herda de ContaBancaria e adiciona funcionalidade de rendimento."""

    def render_juros(self, taxa: float) -> float:
        self._saldo += self._saldo * taxa
        return self._saldo