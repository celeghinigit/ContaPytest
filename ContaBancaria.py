# ContaBancaria.py

class ContaBancaria:
    """Classe base para os diferentes tipos de conta bancária."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        """Retorna o saldo atual da conta."""
        return self._saldo

    def depositar(self, valor: float) -> float:
        """Adiciona um valor positivo ao saldo e retorna o novo saldo."""
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self._saldo += valor
        return self._saldo

    def sacar(self, valor: float) -> float:
        """Retira um valor, desde que haja saldo suficiente."""
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        self._saldo -= valor
        return self._saldo
