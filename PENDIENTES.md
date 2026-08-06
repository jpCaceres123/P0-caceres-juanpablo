# PENDIENTES — Proyecto P0 (MatMul)

Este archivo es una nota de traspaso. Sirve para dar contexto a la IA de
OpenCode que continúe el trabajo: qué es el proyecto, qué está hecho, qué
falta y cómo trabajar. Léelo completo antes de empezar a modificar código.

## 1. Contexto del trabajo

- Proyecto académico individual: implementar una **multiplicación de matrices
  propia** (`mimatmul`) y comparar su rendimiento contra `numpy`.
- Tiene dos entregas: **P0E1** (configuración e inicio) y **P0E2**
  (benchmark, gráfico y documentación final).
- P0E1 ya fue entregada (commit `c10de9f`). Lo que queda es P0E2.
- Repositorio público: https://github.com/jpCaceres123/P0-caceres-juanpablo
- Entrega en Canvas: enlace al repo + hash corto del commit + frase de estado.
- Estudiante: **Juan Pablo Caceres** — usuario GitHub `jpCaceres123`.
- Fecha de P0E1: viernes 7 de agosto de 2026. Revisar la fecha de P0E2 en Canvas.

## 2. Qué está hecho (P0E1, commit `c10de9f`)

- Repositorio `P0-caceres-juanpablo` público en GitHub, con `.gitignore`
  (ignora `.venv/`), `requirements.txt` y al menos 2 commits.
- `README.md`: propósito, SO, versión de Python, comandos del ambiente
  virtual, estado actual.
- `AGENTS.md`: reglas para OpenCode.
- `src/mimatmul.py`: primera versión de `mimatmul(A, B)` con algoritmo de
  triple bucle, validaciones de dimensiones y de tipo.
- `tests/test_mimatmul.py`: 5 pruebas que pasan (multiplicación 2x2,
  identidad, 1x1, dimensiones incompatibles, tipos incorrectos).
- `src/system_info.py`: genera `data/system_info.json` con SO, arquitectura,
  versión de Python, procesador, núcleos físicos/lógicos y RAM.
- Ambiente: Python 3.14.6, Git 2.55, ambiente virtual `.venv`.
- Dependencias instaladas: `pytest`, `psutil`.

## 3. ADVERTENCIA IMPORTANTE sobre la información del computador

`data/system_info.json` fue generado en **otra computadora** (no la del
estudiante). Contiene: Intel Core i3-10105F, 8 núcleos lógicos / 4 físicos,
15.87 GB RAM, Windows 10 Pro.

**Al continuar en la computadora real del estudiante hay que:**
1. Ejecutar `python src/system_info.py` para regenerar el JSON con los datos
   verdaderos de esa máquina.
2. Actualizar `README.md` si cambia el sistema operativo o la versión de
   Python.
3. Hacer un commit con esos cambios.

## 4. Lo que falta para P0E2

- [ ] Regenerar `data/system_info.json` en la computadora real y actualizar
      el README (ver sección 3).
- [ ] Terminar `mimatmul` si el enunciado general lo exige (casos borde y
      rendimiento). Hoy cumple lo básico con triple bucle.
- [ ] Completar todas las pruebas exigidas por el enunciado general.
- [ ] Benchmark definitivo con **cuatro tamaños de matrices** comparando
      `mimatmul` contra `numpy`.
- [ ] Guardar los resultados en un **archivo CSV definitivo**.
- [ ] Generar el **gráfico final** de la comparación (revisar si el enunciado
      pide escala logarítmica).
- [ ] Análisis de **CPU y RAM** durante el benchmark.
- [ ] `README.md` final con resultados, gráfico y **respuestas sobre
      OpenCode** (revisar las preguntas exactas del enunciado general).
- [ ] Commit final de P0E2 y entrega en Canvas (nombre, enlace, hash corto,
      frase de estado).

## 5. Cómo trabajar (reglas para la IA de OpenCode)

- Leer el enunciado general de la tarea si está disponible antes de asumir
  requisitos (tamaños de matrices, formato CSV, preguntas finales).
- Ejecutar las pruebas después de modificar código:
  ```
  pytest
  ```
  (desde el ambiente virtual, en PowerShell: `.\.venv\Scripts\Activate.ps1`).
- **No inventar mediciones**: los tiempos, CSV y gráfico deben salir de
  ejecutar el benchmark real, nunca de números supuestos.
- Mantener el código sencillo y legible. Respetar el estilo existente.
- Si se agregan `numpy`, `matplotlib` u otras dependencias, registrarlas en
  `requirements.txt` e instalarlas en `.venv`.
- No ejecutar comandos destructivos de Git (force push, rebase,
  reset --hard). No subir credenciales.
- Trabajar de forma incremental: pasos pequeños, commits con mensajes
  claros, verificar con pytest antes de cada commit.
- Guiar al estudiante: explicar brevemente cada paso y qué genera.
