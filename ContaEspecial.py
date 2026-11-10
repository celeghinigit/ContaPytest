
from ContaBancaria import ContaBancaria

class ContaEspecial(ContaBancaria):
    """Herda de ContaBancaria e permite utilizar um limite especial."""

    def __init__(
        self, titular: str, saldo_inicial: float = 0.0, limite: float = 500.0
    ):
        super().__init__(titular, saldo_inicial)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")

        if valor > self._saldo + self.limite:
            raise ValueError("Valor excede o limite disponível.")

        self._saldo -= valor
        return self._saldo
