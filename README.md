# P0-Caceres-JuanPablo

Entrega P0E1 del proyecto de multiplicación de matrices.

## Propósito general del proyecto

Implementar una multiplicación de matrices propia (`mimatmul`), obtener
información del computador y, en una segunda etapa (P0E2), medir y comparar
el rendimiento de `mimatmul` contra `numpy` para distintos tamaños de
matrices, generando un gráfico y un análisis de CPU y RAM.

## Sistema operativo

- Windows 10 Pro (64 bits)

## Versión de Python

- Python 3.14.6

## Ambiente virtual

Crear el ambiente virtual:

```
python -m venv .venv
```

Activarlo en Windows con PowerShell:

```
.\.venv\Scripts\Activate.ps1
```

Activarlo en Windows con cmd:

```
.venv\Scripts\activate.bat
```

Instalar las dependencias:

```
pip install -r requirements.txt
```

## Estado actual del proyecto

- Ambiente configurado: Python, Git, GitHub, OpenCode y editor.
- `src/system_info.py` genera `data/system_info.json` con la información
  del computador (sistema operativo, arquitectura, versión de Python,
  procesador, núcleos y memoria RAM).
- Primera versión de `mimatmul(A, B)` en `src/mimatmul.py`.
- Pruebas iniciales en `tests/test_mimatmul.py` (se ejecutan con `pytest`).
- El benchmark, el gráfico y el análisis final se desarrollarán en P0E2.
