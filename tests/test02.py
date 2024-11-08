
import pytest
from es2 import Contobancario  # type: ignore


@pytest.fixture
def conto():
    return Contobancario("123456789", "Mario Rossi", 1000.0)


def test_get_saldo(conto):
    assert conto.get_saldo() == 1000.0


def test_deposita(conto):
    conto.deposita(500.0)
    assert conto.get_saldo() == 1500.0


def test_preleva(conto):
    conto.preleva(200.0)
    assert conto.get_saldo() == 800.0


