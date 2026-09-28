from Backend.banco_de_dados import eleitores
from Frontend.pop_up_aviso import PopUpAviso

class ValidarEleitor():
    def __init__(self, eleitores): 
        super().__init__()
        self.db_eleitores = eleitores
        self.aviso = PopUpAviso()

    def validarEleitor(self, titulo):
        for eleitor in self.db_eleitores:
            if titulo == eleitor["titulo_eleitor"]:
                if eleitor["votou"]:
                    self.aviso.popUp_erro("Este eleitor já votou.")
                    return False
                return True

        self.aviso.popUp_erro("Título de eleitor não encontrado")
        return False