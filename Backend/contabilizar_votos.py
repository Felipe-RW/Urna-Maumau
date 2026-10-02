from Backend import banco_de_dados

class SistemaUrna():

    def __init__(self):
        super().__init__()

        self.db_candidatos = banco_de_dados.candidatos
        self.db_eleitores = banco_de_dados.eleitores

        self.voto_branco = banco_de_dados.votos_brancos
        self.voto_nulo = banco_de_dados.votos_nulos

    
    def contabilizarVoto(self, numero_candidato):

        banco_de_dados.votos_registrados.append(numero_candidato)
        candidato_escolhido = None

        if numero_candidato == "BRANCO":
            banco_de_dados.votos_brancos += 1
            self.voto_branco = banco_de_dados.votos_brancos

        else:

            for candidato in self.db_candidatos:

                if candidato["numero_candidato"] == numero_candidato:
                    candidato_escolhido = candidato
                    break

            if candidato_escolhido != None:
                candidato_escolhido["votos"] += 1

            else:
                banco_de_dados.votos_nulos += 1
                self.voto_nulo = banco_de_dados.votos_nulos