from PySide6.QtCore import QObject, Signal, Slot
from banco_de_dados import candidatos, eleitores
# from zeresima import nulo

class SistemaUrna(QObject): 
    def __init__(self, candidatos, eleitores): 
        super().__init__()
        self.db_candidatos = candidatos
        self.db_eleitores = eleitores

    
    def contabilizarVoto(self, numero_candidato):

        candidato_escolhido = None
        for candidato in self.db_candidatos:
            if candidato["numero_candidato"] == numero_candidato:
                candidato_escolhido = candidato
                break
                
            # if not candidato_escolhido["numero_candidato"]!= numero_candidato:
            #     candidato_nulo = self.zeresima
            #     break

        candidato_escolhido["votos"] += 1
        # candidato_nulo[self.zeresima] += 1