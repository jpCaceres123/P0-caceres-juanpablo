# PENDIENTES — Proyecto P0 (MatMul)

Nota de traspaso y plan de acción. **ESTADO: COMPLETADO (P0E2 lista).**

## Plan de acción completado

### Fase A — Ambiente funcionando

- [x] Verificar `git` y `python` (instalados y configurados).
- [x] Identidad de Git configurada.
- [x] Repositorio clonado en esta computadora.
- [x] Ambiente virtual `.venv` creado y dependencias instaladas
      (`numpy`, `matplotlib`, `pytest`, `psutil`).
- [x] `pytest` pasa (7 pruebas).
- [x] Autenticación de GitHub verificada (push con credenciales guardadas).

### Fase B — Información del computador (regenerada)

- [x] `data/system_info.json` regenerado con los datos reales de esta máquina
      (el anterior era de otra computadora).
- [x] `README.md` actualizado con SO (Windows 11 Home) y Python 3.14.7.

### Fase C — P0E2 (checklist)

- [x] Enunciado general revisado.
- [x] `mimatmul` terminado y revisado.
- [x] Pruebas completadas (7): 2x2 conocido, identidad, 1x1, rectangulares,
      comparación con NumPy, dimensiones incompatibles y tipos incorrectos.
- [x] Benchmark definitivo con 4 tamaños (25, 50, 100, 200): `mimatmul` vs
      `numpy`, 5 repeticiones + calentamiento, `time.perf_counter`.
- [x] Resultados en `data/benchmark_results.csv` (una fila por repetición).
- [x] Gráfico final `figures/benchmark.png` (escala logarítmica en Y).
- [x] Análisis de CPU/RAM/GPU durante el benchmark
      (`data/recursos_durante_benchmark.csv`).
- [x] `README.md` final con resultados, gráfico y reflexión sobre OpenCode.
- [x] Commit final subido a GitHub.

## Entrega final

- Estudiante: Juan Pablo Caceres
- Repositorio: https://github.com/jpCaceres123/P0-caceres-juanpablo
- Hash corto del commit final: `git rev-parse --short HEAD`
- Frase de estado: proyecto completo, pruebas y benchmark verificados.

## Observaciones para el estudiante

- La reflexión de "Uso de OpenCode" en el README debe ser revisada y ajustada
  por ti para reflejar tu propio proceso.
- El equipo estaba con ~88 % de RAM en uso durante las mediciones; si cambia la
  carga del sistema, los tiempos pueden variar ligeramente, pero el orden de
  magnitud se mantiene.
