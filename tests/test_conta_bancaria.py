# test_contas_pytest.py

import pytest

from ContaBancaria import ContaBancaria
from ContaEspecial import ContaEspecial
from ContaPoupanca import ContaPoupanca


# --- FIXTURES (Substituem o setUp) ---
@pytest.fixture
def conta_base():
    return ContaBancaria(titular="Ana", saldo_inicial=100.0)


@pytest.fixture
def conta_especial():
    return ContaEspecial(titular="Maria", saldo_inicial=100.0, limite=500.0)


# --- TESTES DE INICIALIZAÇÃO E OPERAÇÕES BÁSICAS ---
def test_inicializacao_com_sucesso(conta_base):
    assert conta_base.titular == "Ana"
    assert conta_base.saldo == 100.0


def test_inicializacao_saldo_negativo_lanca_excecao():
    with pytest.raises(
        ValueError, match="O saldo inicial não pode ser negativo."
    ):
        ContaBancaria(titular="Carlos", saldo_inicial=-50.0)


def test_deposito_com_valor_valido(conta_base):
    novo_saldo = conta_base.depositar(50.0)
    assert conta_base.saldo == 150.0
    assert novo_saldo == 150.0


# --- TESTES DE HERANÇA E POLIMORFISMO ---
def test_conta_poupanca_herda_metodos_e_adiciona_rendimento():
    poupanca = ContaPoupanca("Carlos", 1000.0)
    poupanca.depositar(500.0)
    assert poupanca.saldo == 1500.0

    poupanca.render_juros(0.01)
    assert poupanca.saldo == 1515.0


def test_saque_conta_especial_com_uso_do_limite(conta_especial):
    conta_especial.sacar(300.0)
    assert conta_especial.saldo == -200.0


def test_saque_conta_especial_excede_limite_total(conta_especial):
    with pytest.raises(ValueError, match="Valor excede o limite disponível."):
        conta_especial.sacar(700.0)
