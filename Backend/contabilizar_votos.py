from banco_de_dados import candidatos, eleitores
# from zeresima import voto_nulo
# from zeresima import voto_branco

class SistemaUrna(): 
    def __init__(self): 
        super().__init__()
        self.db_candidatos = candidatos
        self.db_eleitores = eleitores

    
    def contabilizarVoto(self, numero_candidato):

        candidato_escolhido = None
        if numero_candidato == "BRANCO":
            voto_branco += 1
        else:
            for candidato in self.db_candidatos:
                if candidato["numero_candidato"] == numero_candidato:
                    candidato_escolhido = candidato
                    break

        if candidato_escolhido != None:    
            candidato_escolhido["votos"] += 1
        else:
            voto_nulo += 1