import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class View:
    def __init__(self, controller, root):
        self.__controller = controller

        self.root = tk.Toplevel(root)

        # configura a janela
        self.root.title('Preferências')
        self.root.minsize(400, 300)
        self.root.resizable(False, False)
        #