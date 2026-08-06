"""Obtiene información básica del computador y la guarda en JSON."""

import json
import os
import platform
import sys
from datetime import datetime
from pathlib import Path


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


def obtener_info_sistema():
    info = {
        "fecha_generacion": datetime.now().isoformat(timespec="seconds"),
        "sistema_operativo": platform.system(),
        "plataforma": platform.platform(),
        "arquitectura": platform.machine(),
        "modelo_procesador": obtener_modelo_procesador(),
        "nucleos_logicos": os.cpu_count(),
        "version_python": platform.python_version(),
    }
    try:
        import psutil

        info["nucleos_fisicos"] = psutil.cpu_count(logical=False)
        info["memoria_ram_total_bytes"] = psutil.virtual_memory().total
        info["memoria_ram_total_gb"] = round(
            psutil.virtual_memory().total / (1024 ** 3), 2
        )
    except ImportError:
        info["nucleos_fisicos"] = None
        info["memoria_ram_total_bytes"] = None
        info["memoria_ram_total_gb"] = None
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
