# ContaBancaria.py


class ContaBancaria:
    """Classe Base (Superclasse)."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        else:
            self._saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        else:
            self._saldo += valor
        return self._saldo

    def sacar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        elif valor > self._saldo:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        else:
            self._saldo -= valor
        return self._saldo