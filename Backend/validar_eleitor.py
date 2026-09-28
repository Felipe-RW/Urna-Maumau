from Backend.banco_de_dados import eleitores
from Frontend.pop_up_aviso import PopUpAviso

class ValidarEleitor():
    def __init__(self, candidatos, eleitores): 
        super().__init__()
        self.db_eleitores = eleitores

    def validarEleitor(self, titulo):
        for eleitor in eleitores:
            if titulo == eleitor["titulo_eleitor"] and not eleitor["votou"]:
                return True
            elif titulo == eleitor["titulo_eleitor"] and eleitor["votou"]:
                