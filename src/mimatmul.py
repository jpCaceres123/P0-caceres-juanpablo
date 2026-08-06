"""Implementación propia de multiplicación de matrices."""


def mimatmul(A, B):
    """Multiplica dos matrices A (m x n) y B (n x p) con un algoritmo de triple bucle.

    Parámetros:
        A: lista de listas (m x n).
        B: lista de listas (n x p).

    Devuelve:
        Lista de listas (m x p) con el producto A @ B.

    Lanza:
        TypeError: si A o B no son listas.
        ValueError: si las matrices están vacías, no son rectangulares o
            tienen dimensiones incompatibles.
    """
    if not isinstance(A, list) or not isinstance(B, list):
        raise TypeError("A y B deben ser listas de listas")

    if len(A) == 0 or len(B) == 0:
        raise ValueError("las matrices no pueden estar vacías")

    filas_a = len(A)
    cols_a = len(A[0])
    filas_b = len(B)
    cols_b = len(B[0])

    for fila in A:
        if not isinstance(fila, list) or len(fila) != cols_a:
            raise ValueError("A debe ser una matriz rectangular")
    for fila in B:
        if not isinstance(fila, list) or len(fila) != cols_b:
            raise ValueError("B debe ser una matriz rectangular")

    if cols_a != filas_b:
        raise ValueError(
            "dimensiones incompatibles: "
            f"A es {filas_a}x{cols_a} y B es {filas_b}x{cols_b}"
        )

    resultado = [[0] * cols_b for _ in range(filas_a)]
    for i in range(filas_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += A[i][k] * B[k][j]
            resultado[i][j] = total
    return resultado
