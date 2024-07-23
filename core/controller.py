from core.model import Model
from core.view import View

from core.settings.controller import Controller as ctrlSettings

class Controller:
    def __init__(self):
        self.__model = Model()
        self.__view = View(self)

    # rotina de encerramento do programa
    def safe_exit(self):
        print('Encerrando aplicação...')
    #

    # inicia a janela de preferências
    def open_settings(self, root):
        ctrlSettings.make_window(self, root)
    #