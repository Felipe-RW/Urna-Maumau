from Backend.banco_de_dados import eleitores
from Frontend.pop_up_aviso import PopUpAviso

class CancelarVoto():
    def __init__(self, eleitor):
        super().__init__()
        self.eleitor = eleitor
        self.aviso = PopUpAviso()

    def cancelarVoto(self, titulo):
        if self.aviso.popupConfirmacao(titulo):
            self.eleitor["votou"] = False
            return True
        return False