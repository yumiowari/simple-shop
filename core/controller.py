from core.model import Model
from core.view import View

class Controller:
    def __init__(self):
        self.__model = Model()
        self.__view = View(self)

    # rotina de encerramento do programa
    def safe_exit(self):
        print('Encerrando aplicação...')
    #