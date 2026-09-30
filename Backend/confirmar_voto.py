from Backend.banco_de_dados import candidatos, eleitores
from pathlib import Path
import sys
from Backend.validar_eleitor import ValidarEleitor
from Backend.contabilizar_votos import SistemaUrna
from Frontend.pop_up_aviso import PopUpAviso
from Frontend.tela_finalizacao import TelaFinalizacao

root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

class ConfirmarVotos():
    def __init__(self):
        super().__init__()
        self.lista_candidatos = candidatos
        self.lista_eleitores = eleitores
        self.validar_eleitor= ValidarEleitor(eleitores)
        self.contabilizar_votos= SistemaUrna(candidatos, eleitores)
        self.popup = PopUpAviso()
        self.tela_finalizacao = TelaFinalizacao()

    def submeterVotos(self, numero_candidato):
        self.contabilizar_votos.contabilizarVoto(numero_candidato)
        self.tela_finalizacao.show()

       



