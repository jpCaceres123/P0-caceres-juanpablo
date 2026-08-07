"""Benchmark: compara mimatmul contra numpy (A @ B).

Genera:
- data/benchmark_results.csv        (una fila por repetición)
- data/recursos_durante_benchmark.csv  (muestreos de CPU/RAM/GPU)
- figures/benchmark.png             (tiempo vs tamaño para ambos métodos)

Uso:
    python src/benchmark.py
"""

import csv
import shutil
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from mimatmul import mimatmul  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
RUTA_CSV = RAIZ / "data" / "benchmark_results.csv"
RUTA_RECURSOS = RAIZ / "data" / "recursos_durante_benchmark.csv"
RUTA_FIGURA = RAIZ / "figures" / "benchmark.png"

TAMANOS = [25, 50, 100, 200]
REPETICIONES = 5
WARMUP = 1
INTERVALO_MONITOR = 0.25


def _calentamiento(metodo, matriz, matriz_lista, repeticiones):
    for _ in range(repeticiones):
        if metodo == "mimatmul":
            mimatmul(matriz_lista, matriz_lista)
        else:
            matriz @ matriz


def tiempo_mimatmul(matriz_lista):
    t0 = time.perf_counter()
    mimatmul(matriz_lista, matriz_lista)
    t1 = time.perf_counter()
    return t1 - t0


def tiempo_numpy(matriz):
    t0 = time.perf_counter()
    matriz @ matriz
    t1 = time.perf_counter()
    return t1 - t0


def medir(metodo, matriz, matriz_lista):
    if metodo == "mimatmul":
        return tiempo_mimatmul(matriz_lista)
    return tiempo_numpy(matriz)


class MonitorRecursos:
    """Muestrea CPU, RAM y GPU mientras corre el benchmark."""

    def __init__(self, intervalo=INTERVALO_MONITOR):
        self.intervalo = intervalo
        self._detener = threading.Event()
        self._hilo = threading.Thread(target=self._muestrear, daemon=True)
        self.muestras = []
        self.hora_inicio = None

    def _muestrear(self):
        import psutil

        self.hora_inicio = time.perf_counter()
        psutil.cpu_percent(interval=None)
        while not self._detener.is_set():
            muestreo = {
                "tiempo_relativo_seg": round(
                    time.perf_counter() - self.hora_inicio, 2
                ),
                "cpu_porcentaje": psutil.cpu_percent(interval=0),
                "ram_porcentaje": psutil.virtual_memory().percent,
                "ram_disponible_gb": round(
                    psutil.virtual_memory().available / (1024 ** 3), 2
                ),
            }
            muestreo["gpu_utilizacion"] = self._gpu_utilizacion()
            self.muestras.append(muestreo)
            time.sleep(self.intervalo)

    @staticmethod
    def _gpu_utilizacion():
        if shutil.which("nvidia-smi") is None:
            return "no disponible"
        try:
            resultado = subprocess.run(
                [
                    "nvidia-smi",
                    "--query-gpu=utilization.gpu",
                    "--format=csv,noheader,nounits",
                ],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return float(resultado.stdout.strip())
        except (OSError, subprocess.SubprocessError, ValueError):
            return "no disponible"

    def iniciar(self):
        self._hilo.start()

    def detener(self):
        self._detener.set()
        self._hilo.join(timeout=2)

    def resumen(self):
        if not self.muestras:
            return {}
        cpu = [m["cpu_porcentaje"] for m in self.muestras]
        ram = [m["ram_porcentaje"] for m in self.muestras]
        gpu = [
            m["gpu_utilizacion"]
            for m in self.muestras
            if isinstance(m["gpu_utilizacion"], (int, float))
        ]
        resumen = {
            "duracion_seg": round(
                self.muestras[-1]["tiempo_relativo_seg"], 2
            ),
            "cpu_promedio_porcentaje": round(sum(cpu) / len(cpu), 1),
            "cpu_maximo_porcentaje": max(cpu),
            "ram_promedio_porcentaje": round(sum(ram) / len(ram), 1),
            "ram_maximo_porcentaje": max(ram),
        }
        if gpu:
            resumen["gpu_promedio_utilizacion"] = round(sum(gpu) / len(gpu), 1)
            resumen["gpu_maximo_utilizacion"] = max(gpu)
        else:
            resumen["gpu_promedio_utilizacion"] = "no disponible"
        return resumen


def ejecutar_benchmark():
    rng = np.random.default_rng(20260806)
    filas = []
    for tamanio in TAMANOS:
        matriz = rng.standard_normal((tamanio, tamanio)).astype(np.float64)
        matriz_lista = matriz.tolist()
        for metodo, m, ml in (
            ("mimatmul", matriz, matriz_lista),
            ("numpy", matriz, matriz_lista),
        ):
            _calentamiento(metodo, m, ml, WARMUP)
        for repeticion in range(1, REPETICIONES + 1):
            for metodo, m, ml in (
                ("mimatmul", matriz, matriz_lista),
                ("numpy", matriz, matriz_lista),
            ):
                tiempo = medir(metodo, m, ml)
                filas.append(
                    {
                        "tamano": tamanio,
                        "metodo": metodo,
                        "repeticion": repeticion,
                        "tiempo_segundos": round(tiempo, 8),
                    }
                )
                print(f"tamano={tamanio} metodo={metodo} "
                      f"repeticion={repeticion} tiempo={tiempo:.6f} s")
    return filas


def guardar_csv(filas, ruta):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=["tamano", "metodo", "repeticion", "tiempo_segundos"],
        )
        escritor.writeheader()
        escritor.writerows(filas)


def guardar_csv_recursos(monitor, ruta):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=[
                "tiempo_relativo_seg",
                "cpu_porcentaje",
                "ram_porcentaje",
                "ram_disponible_gb",
                "gpu_utilizacion",
            ],
        )
        escritor.writeheader()
        escritor.writerows(monitor.muestras)


def generar_figura(filas, ruta):
    datos = {}
    for metodo in ("mimatmul", "numpy"):
        datos[metodo] = {}
        for fila in filas:
            if fila["metodo"] != metodo:
                continue
            datos[metodo].setdefault(fila["tamano"], []).append(
                fila["tiempo_segundos"]
            )

    fig, eje = plt.subplots(figsize=(8, 5))
    for metodo, color in (("mimatmul", "tab:red"), ("numpy", "tab:blue")):
        tamanos = sorted(datos[metodo])
        tiempos = [np.mean(datos[metodo][t]) for t in tamanos]
        eje.plot(tamanos, tiempos, marker="o", color=color, label=metodo)

    eje.set_xlabel("Tamaño de la matriz (n x n)")
    eje.set_ylabel("Tiempo de ejecución (s, escala logarítmica)")
    eje.set_title("Benchmark: mimatmul vs numpy (promedio de repeticiones)")
    eje.set_yscale("log")
    eje.grid(True, which="both", linestyle="--", alpha=0.5)
    eje.legend()
    fig.tight_layout()
    ruta.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ruta, dpi=150)
    plt.close(fig)


def main():
    monitor = MonitorRecursos()
    monitor.iniciar()
    filas = ejecutar_benchmark()
    monitor.detener()

    guardar_csv(filas, RUTA_CSV)
    guardar_csv_recursos(monitor, RUTA_RECURSOS)
    generar_figura(filas, RUTA_FIGURA)

    resumen = monitor.resumen()
    print("\nResumen de recursos durante el benchmark:")
    print(resumen)
    print(f"\nCSV guardado en: {RUTA_CSV}")
    print(f"CSV de recursos guardado en: {RUTA_RECURSOS}")
    print(f"Figura guardada en: {RUTA_FIGURA}")
    print(f"Generado el: {datetime.now().isoformat(timespec='seconds')}")


if __name__ == "__main__":
    main()
