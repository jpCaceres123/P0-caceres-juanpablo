# PENDIENTES — Proyecto P0 (MatMul)

Este archivo es una nota de traspaso y un **plan de acción**. La IA de
OpenCode que continúe este trabajo debe leerlo completo y ejecutar el plan de
forma **autónoma**, sin pedir permiso para cada paso. Solo debe consultar al
estudiante si algo la bloquea o necesita datos que no están en el repositorio.

## 0. PLAN DE ACCIÓN (ejecutar en orden, verificando cada paso)

### Fase A — Dejar el ambiente funcionando en esta computadora

1. Verificar que existen `git` y `python` (ejecutar `git --version` y
   `python --version`).
2. Si falta alguno, instalarlo con winget:
   ```
   winget install Git.Git
   winget install Python.Python.3.14
   ```
   Puede aparecer un aviso de "permiso de administrador": pedirle al
   estudiante que haga clic en **Sí**. Si no se encuentra `git`/`python`
   después de instalar, usar las rutas completas (p. ej.
   `C:\Program Files\Git\cmd\git.exe` y
   `C:\Users\<usuario>\AppData\Local\Programs\Python\Python314\python.exe`).
3. Configurar la identidad de Git si no está:
   ```
   git config --global user.name "Juan Pablo Caceres"
   git config --global user.email "jpcaceres3@miuandes.cl"
   ```
4. Clonar el repositorio si no está clonado:
   ```
   git clone https://github.com/jpCaceres123/P0-caceres-juanpablo.git
   cd P0-caceres-juanpablo
   ```
   (Si ya está clonado, abrir esa carpeta y ejecutar `git pull`.)
5. Crear el ambiente virtual e instalar dependencias:
   ```
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
6. Ejecutar las pruebas: `pytest`. **Deben pasar las 5 pruebas existentes.**
7. Verificar la autenticación de GitHub para poder hacer push (sin esto,
   `git push` va a fallar):
   - Ejecutar `gh auth status`. Si falla, instalar la CLI de GitHub
     (`winget install GitHub.cli`) y ejecutar `gh auth login`.
   - `gh auth login` es **interactivo y requiere al estudiante**: pedirle
     que complete el login en el navegador con su cuenta `jpCaceres123`.
     Es la única acción manual ineludible (GitHub lo exige).

### Fase B — Corregir la información del computador (obligatorio)

`data/system_info.json` fue generado en OTRA computadora (Intel Core
i3-10105F, 8 núcleos lógicos, 15.87 GB RAM, Windows 10 Pro). Hay que
regenerarlo con los datos reales de esta máquina:

1. Ejecutar `python src/system_info.py`.
2. Si el sistema operativo o la versión de Python cambian respecto del
   `README.md`, actualizar esas líneas en `README.md`.
3. Hacer commit y push de esos cambios.

### Fase C — Completar P0E2 (checklist)

1. Revisar el **enunciado general de la tarea** si el estudiante lo entrega
   (tamaños de matrices, formato del CSV, preguntas finales sobre OpenCode).
2. Terminar `mimatmul` si el enunciado lo exige (casos borde y rendimiento).
3. Completar todas las pruebas exigidas por el enunciado.
4. Benchmark definitivo con **cuatro tamaños de matrices**: `mimatmul` vs
   `numpy`. Agregar `numpy` y `matplotlib` a `requirements.txt` e instalarlos
   en `.venv` cuando se usen.
5. Guardar los resultados en un **archivo CSV definitivo** (por ejemplo en
   `data/`).
6. Generar el **gráfico final** de la comparación (revisar si el enunciado
   pide escala logarítmica).
7. Análisis de **CPU y RAM** durante el benchmark.
8. `README.md` final con resultados, gráfico y **respuestas sobre OpenCode**.
9. Hacer commit final de P0E2, subirlo a GitHub y entregar al estudiante:
   - nombre: Juan Pablo Caceres;
   - enlace al repo: https://github.com/jpCaceres123/P0-caceres-juanpablo;
   - hash corto del commit (`git rev-parse --short HEAD`);
   - frase de estado.

## 1. Contexto del trabajo

- Proyecto académico individual: implementar una **multiplicación de matrices
  propia** (`mimatmul`) y comparar su rendimiento contra `numpy`.
- Tiene dos entregas: **P0E1** (configuración e inicio) y **P0E2**
  (benchmark, gráfico y documentación final).
- P0E1 ya fue entregada (commit `c10de9f`). Lo que queda es P0E2.
- Repositorio público: https://github.com/jpCaceres123/P0-caceres-juanpablo
- Entrega en Canvas: enlace al repo + hash corto del commit + frase de estado.
- Estudiante: **Juan Pablo Caceres** — usuario GitHub `jpCaceres123`.
- Fecha de P0E1: viernes 7 de agosto de 2026. Revisar la fecha de P0E2 en
  Canvas.

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

## 3. Cómo trabajar (reglas)

- Ejecutar las pruebas después de modificar código:
  ```
  pytest
  ```
  (desde el ambiente virtual: `.\.venv\Scripts\Activate.ps1`).
- **No inventar mediciones**: los tiempos, CSV y gráfico deben salir de
  ejecutar el benchmark real, nunca de números supuestos.
- Mantener el código sencillo y legible. Respetar el estilo existente.
- Si se agregan `numpy`, `matplotlib` u otras dependencias, registrarlas en
  `requirements.txt` e instalarlas en `.venv`.
- No ejecutar comandos destructivos de Git (force push, rebase,
  reset --hard). No subir credenciales.
- Trabajar de forma incremental: pasos pequeños, commits con mensajes
  claros, verificar con pytest antes de cada commit.
- Informar al estudiante al final: qué se hizo, qué archivos se generaron,
  hash del commit final y qué falta (si queda algo).
