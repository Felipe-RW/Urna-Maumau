from banco_de_dados import candidatos, eleitores
# from zeresima import voto_nulo
# from zeresima import voto_branco

class SistemaUrna():

    def __init__(self):
        super().__init__()

        self.db_candidatos = candidatos
        self.db_eleitores = eleitores

        self.voto_branco = 0
        self.voto_nulo = 0

    
    def contabilizarVoto(self, numero_candidato):

        candidato_escolhido = None

        if numero_candidato == "BRANCO":
            self.voto_branco += 1

        else:

            for candidato in self.db_candidatos:

                if candidato["numero_candidato"] == numero_candidato:
                    candidato_escolhido = candidato
                    break

            if candidato_escolhido != None:
                candidato_escolhido["votos"] += 1

            else:
                self.voto_nulo += 1