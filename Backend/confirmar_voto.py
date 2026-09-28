from PySide6.QtCore import QObject, Signal, Slot
from banco_de_dados import candidatos, eleitores

class ConfirmarVotos(QObject):
    voto_confirmado = Signal()
    voto_negado = Signal()

    def __init__(self, candidatos, eleitores):
        super().__init__()
        self.lista_candidatos = candidatos
        self.lista_eleitores = eleitores

    @Slot(int) 
    def submeterVotos(self, titulo_eleitor):
        for eleitor in self.lista_eleitores:
            if eleitor["titulo_eleitor"] == titulo_eleitor:
                
                if eleitor["votou"] == True:
                    self.voto_negado.emit()
                    return
                
                eleitor["votou"] = True
                self.voto_confirmado.emit()
                return  