from banco_de_dados import candidatos, eleitores
from Backend.validar_eleitor import ValidarEleitor
from Backend.contabilizar_votos import SistemaUrna
from Frontend.pop_up_aviso import PopUpAviso

class ConfirmarVotos():
    def __init__(self):
        super().__init__()
        self.lista_candidatos = candidatos
        self.lista_eleitores = eleitores
        self.validar_eleitor= ValidarEleitor(eleitores)
        self.contabilizar_votos = SistemaUrna()
        self.popup = PopUpAviso()

    def submeterVotos(self, numero_candidato):
        self.contabilizar_votos.contabilizarVoto(numero_candidato)
        #PopUp de fim e depois voltar para tela principal urna

       



