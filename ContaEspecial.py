# ContaEspecial.py
from ContaBancaria import ContaBancaria


class ContaEspecial(ContaBancaria):
    """Conta que permite saques utilizando um limite adicional."""

    def __init__(
        self, titular: str, saldo_inicial: float = 0.0, limite: float = 500.0
    ):
        super().__init__(titular, saldo_inicial)
        if limite < 0:
            raise ValueError("O limite não pode ser negativo.")
        self.limite = limite

    def sacar(self, valor: float) -> float:
        """Saca até o saldo disponível somado ao limite da conta."""
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self._saldo + self.limite:
            raise ValueError("Valor excede o limite disponível.")
        self._saldo -= valor
        return self._saldo
