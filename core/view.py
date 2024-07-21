import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

        # menu
        self.__menu = tk.Menu(self.root)
        
        self.__app_menu = tk.Menu(self.__menu, tearoff = 0)
        self.__app_menu.add_command(label = 'Preferências')
        self.__app_menu.add_separator()
        self.__app_menu.add_command(label = 'Sair', command = self.safe_exit)

        self.__menu.add_cascade(menu = self.__app_menu, label = 'App')

        self.root.configure(menu = self.__menu)
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

    # rotina de encerramento do programa
    def safe_exit(self):
        if messagebox.askyesno(title = 'Confirmação', message = 'Deseja encerrar o programa?', icon = 'warning'):
            self.__controller.safe_exit()

            self.root.destroy()
    #