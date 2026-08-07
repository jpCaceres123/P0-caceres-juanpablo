# AGENTS.md

Instrucciones permanentes para agentes de OpenCode que trabajen en este
repositorio.

## Propósito del proyecto

Implementar una multiplicación de matrices propia (`mimatmul`) y comparar su
rendimiento con `numpy` (operación `A @ B`), generando mediciones reales,
gráficos y documentación. Proyecto académico correspondiente a las entregas
P0E1 y P0E2.

## Instrucción principal

Antes de trabajar, leé `PENDIENTES.md` completo y seguí su **plan de acción**
de forma **autónoma**, verificando cada paso (instalaciones, clones, venv,
pytest, commits, push) sin pedir permiso al estudiante. Solo consultalo si algo
te bloquea o necesitás datos que no están en el repositorio.

## Estructura del repositorio

```
├── README.md                 Instrucciones para instalar y ejecutar
├── AGENTS.md                 Instrucciones para OpenCode
├── PENDIENTES.md             Nota de traspaso y plan de acción
├── pytest.ini                Configuración de pytest (pythonpath=src)
├── requirements.txt          Dependencias del proyecto
├── src/
│   ├── system_info.py        Información del computador -> data/system_info.json
│   ├── mimatmul.py           Multiplicación de matrices con ciclos de Python
│   └── benchmark.py          Benchmark mimatmul vs numpy (CSV + gráfico)
├── tests/
│   └── test_mimatmul.py      Pruebas de mimatmul
├── data/                     Datos generados (system_info.json, CSV del benchmark)
└── figures/                  Gráficos generados (benchmark.png)
```

## Reglas

- Mantener el código sencillo y legible.
- Ejecutar las pruebas después de modificar código:
  ```
  pytest
  ```
  (desde el ambiente virtual: `.\.venv\Scripts\Activate.ps1`).
- **No inventar mediciones ni datos**: los tiempos, CSV y gráficos deben salir
  de ejecutar el código real, nunca de números supuestos.
- **Conservar los datos originales**: no editar manualmente los CSV ni el JSON
  generados; si un dato cambió, regenerarlo ejecutando el script.
- **No crear matrices que puedan agotar la memoria**: usar tamaños moderados
  y verificar la memoria disponible antes de aumentar tamaños.
- No ejecutar comandos destructivos de Git (force push, rebase, reset --hard).
- No subir credenciales ni información sensible.
- Trabajar de forma incremental: pasos pequeños, commits con mensajes claros.
- **El estudiante debe revisar los cambios antes de hacer commit o push**:
  avisarle qué se modificó y esperar su confirmación cuando sea posible.
- Informar al estudiante al final: qué se hizo, qué archivos se generaron,
  hash del commit final y qué falta (si queda algo).
