from core.settings.model import Model
from core.settings.view import View

class Controller:
    def __init__(self):
        self.__model = Model()

    # inicia a janela
    def make_window(self, root):
        self.__view = View(self, root)
    #
