import tkinter as tk
import platform
import psutil
import gpuinfo
import tkinter as tk
import GPUtil
from tkinter import messagebox
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
        gpu = GPUtil.getGPUs()[0]
        system_info += f"Carte graphique:\n"
        system_info += f"- Nom: {gpu.name}\n"
        system_info += f"- VRAM totale: {gpu.memoryTotal} MB\n"
    except Exception as e:
        system_info += "Carte graphique: Informations non disponibles\n"

    return system_info

def check_updates():
    memory_info = psutil.virtual_memory()
    if memory_info.total < 4 * 1024**3:
        messagebox.showinfo("Mises à jour nécessaires", "Une mise à jour de la mémoire RAM est nécessaire.")
    else:
        messagebox.showinfo("Mises à jour nécessaires", "Aucune mise à jour n'est nécessaire.")

def update_info():
    system_info_label.config(text=get_system_info())

root = tk.Tk()
root.title("Vérification des composants du PC")

system_info_label = tk.Label(root, text=get_system_info(), padx=10, pady=10, justify='left')
system_info_label.pack()

update_button = tk.Button(root, text="Mettre à jour", command=update_info)
update_button.pack()

check_updates_button = tk.Button(root, text="Vérifier les mises à jour", command=check_updates)
check_updates_button.pack()

exit_button = tk.Button(root, text="Quitter", command=root.quit)
exit_button.pack()

root.mainloop()
