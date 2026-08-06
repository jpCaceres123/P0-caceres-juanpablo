import pytest

from mimatmul import mimatmul


def test_multiplicacion_2x2():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    esperado = [[19, 22], [43, 50]]
    assert mimatmul(A, B) == esperado


def test_multiplicacion_por_identidad():
    A = [[2, 0, 1], [3, 0, 0], [5, 1, 1]]
    identidad = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert mimatmul(A, identidad) == A


def test_matriz_un_elemento():
    A = [[3]]
    B = [[4]]
    assert mimatmul(A, B) == [[12]]


def test_dimensiones_incompatibles():
    A = [[1, 2]]
    B = [[1, 2, 3]]
    with pytest.raises(ValueError):
        mimatmul(A, B)


def test_tipos_incorrectos():
    with pytest.raises(TypeError):
        mimatmul("no", [[1]])
