import numpy as np
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


def test_matrices_rectangulares():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    esperado = [[58, 64], [139, 154]]
    assert mimatmul(A, B) == esperado


def test_comparacion_con_numpy():
    rng = np.random.default_rng(42)
    casos = [(5, 5), (3, 7, 2), (1, 1), (6, 4, 9)]
    for caso in casos:
        if len(caso) == 2:
            m, n = caso
            p = m
        else:
            m, n, p = caso
        A = rng.standard_normal((m, n))
        B = rng.standard_normal((n, p))
        resultado = mimatmul(A.tolist(), B.tolist())
        esperado = A @ B
        assert np.allclose(resultado, esperado, atol=1e-9)
