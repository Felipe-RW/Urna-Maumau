from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QMessageBox
from banco_de_dados import candidatos, eleitores
from Backend.validar_eleitor import ValidarEleitor
from Backend.contabilizar_votos import SistemaUrna
from Frontend.pop_up_aviso import PopUpAviso

class ConfirmarVotos(QObject):
    def __init__(self, candidatos, eleitores):
        super().__init__()
        self.lista_candidatos = candidatos
        self.lista_eleitores = eleitores
        self.validar_eleitor= ValidarEleitor(eleitores)
        self.contabilizar_votos= SistemaUrna(candidatos, eleitores)
        self.popup = PopUpAviso()

    def submeterVotos(self, titulo_eleitor, numero_candidato):
        self.contabilizar_votos.contabilizarVoto(numero_candidato)

                  

       



