import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, controller):
        self.__controller = controller

        # faz a janela
        self.root = tk.Tk()
        #

        # configura a janela
        self.root.title('$imple $hop')
        self.root.minsize(400, 300)
        self.root.resizable(False, False)
        self.centrazile()
        #

        # inicia a janela
        self.root.mainloop()
        #
    
    # faz a janela aparecer no meio da tela
    def centrazile(self):
        x = int((self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2) # média da largura da tela com a largura da janela
        y = int((self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2) # média da altura da tela com a altura da janela

        self.root.geometry(f'+{x}+{y}')
    #