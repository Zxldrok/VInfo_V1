import platform
import psutil
from GPUtil import getGPUs
import cpuinfo

def get_system_info():
    system_info = f"Système: {platform.system()} {platform.release()}\n\n"

    try:
        cpu_info = cpuinfo.get_cpu_info()
        system_info += f"Processeur:\n"
        system_info += f"- Nom: {cpu_info['brand_raw']}\n"
        system_info += f"- Architecture: {cpu_info['arch']}\n"
        system_info += f"- Fréquence: {cpu_info['hz_actual_raw']}\n"
        system_info += f"- Cœurs physiques: {psutil.cpu_count(logical=False)}\n"
        system_info += f"- Cœurs logiques: {psutil.cpu_count(logical=True)}\n\n"
    except Exception as e:
        system_info += "Processeur: Informations non disponibles\n\n"

    system_info += f"Mémoire:\n"
    system_info += f"- Mémoire totale: {psutil.virtual_memory().total / (1024**3):.2f} Go\n"
    system_info += f"- Utilisation du processeur: {psutil.cpu_percent()}%\n"
    system_info += f"- Utilisation de la mémoire: {psutil.virtual_memory().percent}%\n\n"

    try:
        gpu = getGPUs()[0]
        system_info += f"Carte graphique:\n"
        system_info += f"- Nom: {gpu.name}\n"
        system_info += f"- VRAM totale: {gpu.memoryTotal} MB\n"
    except Exception as e:
        system_info += "Carte graphique: Informations non disponibles\n"

    return system_info
