# ContaEspecial.py
from ContaBancaria import ContaBancaria
class ContaEspecial(ContaBancaria):
    """Herda de ContaBancaria e sobrescreve o comportamento de saque para permitir uso de limite."""

    def __init__(
        self, titular: str, saldo_inicial: float = 0.0, limite: float = 500.0
    ):
        super().__init__(titular, saldo_inicial)
        self.limite = limite

    # Polimorfismo: sobrescreve o método sacar() da superclasse
    def sacar(self, valor: float) -> float:
        if valor > self.limite:
            raise ValueError("Valor excede o limite disponível.")
        else:
            self._saldo -= valor
            return self._saldo