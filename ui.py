import tkinter as tk
from tkinter import messagebox
import psutil
from system_info import get_system_info

def update_info(system_info_label):
    system_info_label.config(text=get_system_info())

def check_updates():
    memory_info = psutil.virtual_memory()
    if memory_info.total < 4 * 1024**3:
        messagebox.showinfo("Mises à jour nécessaires", "Une mise à jour de la mémoire RAM est nécessaire.")
    else:
        messagebox.showinfo("Mises à jour nécessaires", "Aucune mise à jour n'est nécessaire.")

def create_gui(root):
    root.title("Vérification des composants du PC")

    system_info_label = tk.Label(root, text=get_system_info(), padx=10, pady=10, justify='left')
    system_info_label.pack()

    update_button = tk.Button(root, text="Mettre à jour", command=lambda: update_info(system_info_label))
    update_button.pack()

    check_updates_button = tk.Button(root, text="Vérifier les mises à jour", command=check_updates)
    check_updates_button.pack()

    exit_button = tk.Button(root, text="Quitter", command=root.quit)
    exit_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    create_gui(root)
    root.mainloop()
