import tkinter as tk
from ui import create_gui

def main():
    root = tk.Tk()
    root.title("Vérification des composants du PC")
    create_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
