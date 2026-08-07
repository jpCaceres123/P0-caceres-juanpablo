"""Obtiene información básica del computador y la guarda en JSON."""

import json
import os
import platform
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def _valor_no_disponible():
    return "no disponible"


def obtener_modelo_procesador():
    if sys.platform == "win32":
        try:
            import winreg

            clave = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"HARDWARE\DESCRIPTION\System\CentralProcessor\0",
            )
            valor, _ = winreg.QueryValueEx(clave, "ProcessorNameString")
            winreg.CloseKey(clave)
            return valor.strip()
        except OSError:
            pass
    return platform.processor()


def obtener_modelo_gpu():
    if sys.platform != "win32":
        return _valor_no_disponible()
    try:
        resultado = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name",
            ],
            capture_output=True,
            text=True,
            timeout=15,
        )
        modelos = [linea.strip() for linea in resultado.stdout.splitlines() if linea.strip()]
        if not modelos:
            return _valor_no_disponible()
        return modelos
    except (OSError, subprocess.SubprocessError):
        return _valor_no_disponible()


def obtener_disco_principal():
    try:
        raiz = os.path.splitdrive(os.getcwd())[0] + os.sep
        uso = shutil.disk_usage(raiz)
        return {
            "letra": os.path.splitdrive(raiz)[0],
            "capacidad_total_bytes": uso.total,
            "espacio_libre_bytes": uso.free,
            "capacidad_total_gb": round(uso.total / (1024 ** 3), 2),
            "espacio_libre_gb": round(uso.free / (1024 ** 3), 2),
        }
    except OSError:
        return _valor_no_disponible()


def obtener_info_sistema():
    info = {
        "fecha_generacion": datetime.now().isoformat(timespec="seconds"),
        "sistema_operativo": platform.system(),
        "plataforma": platform.platform(),
        "arquitectura": platform.machine(),
        "version_python": platform.python_version(),
        "modelo_procesador": obtener_modelo_procesador(),
        "nucleos_logicos": os.cpu_count(),
    }

    try:
        import numpy

        info["version_numpy"] = numpy.__version__
    except ImportError:
        info["version_numpy"] = _valor_no_disponible()

    try:
        import psutil

        memoria = psutil.virtual_memory()
        info["nucleos_fisicos"] = psutil.cpu_count(logical=False)
        info["memoria_ram_total_bytes"] = memoria.total
        info["memoria_ram_total_gb"] = round(memoria.total / (1024 ** 3), 2)
        info["memoria_ram_disponible_bytes"] = memoria.available
        info["memoria_ram_disponible_gb"] = round(memoria.available / (1024 ** 3), 2)
    except ImportError:
        info["nucleos_fisicos"] = _valor_no_disponible()
        info["memoria_ram_total_bytes"] = _valor_no_disponible()
        info["memoria_ram_total_gb"] = _valor_no_disponible()
        info["memoria_ram_disponible_bytes"] = _valor_no_disponible()
        info["memoria_ram_disponible_gb"] = _valor_no_disponible()

    info["modelo_gpu"] = obtener_modelo_gpu()
    info["disco_principal"] = obtener_disco_principal()
    return info


def main():
    info = obtener_info_sistema()
    ruta_destino = Path(__file__).resolve().parents[1] / "data" / "system_info.json"
    ruta_destino.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta_destino, "w", encoding="utf-8") as archivo:
        json.dump(info, archivo, indent=4, ensure_ascii=False)
    print(json.dumps(info, indent=4, ensure_ascii=False))
    print(f"\nGuardado en: {ruta_destino}")


if __name__ == "__main__":
    main()
