class ApurarResultado:
    def __init__(self):
        self.candidatos = []
        self.eleitores = []
        self.votos_brancos = 0
        self.votos_nulos = 0
        self.eleicao_aberta = True


    def apurarResultado(self):
        if not self.eleicao_aberta:
            return None
        
        total_votos_candidatos = sum(
            candidato["votos"] 
            for candidato in self.candidatos
        )

        total_votos = (
            total_votos_candidatos 
            + self.votos_brancos 
            + self.votos_nulos
        )

        if total_votos > 0:
            percentual_nulos = (
                self.votos_nulos / total_votos
            ) * 100
        else:
            percentual_nulos = 0
        
        candidatos_resultado = []

        for candidato in self.candidatos:

            if total_votos_candidatos > 0:
                percentual = (
                    candidato["votos"]
                    / total_votos_candidatos
                ) * 100
            else:
                percentual = 0

            candidatos_resultado.append({
                "nome": candidato["nome"],
                "numero_candidato": candidato["numero_candidato"],
                "votos": candidato["votos"],
                "percentual": percentual
            })

        if percentual_nulos > 50:
            situacao = "Eleição anulada"
            vencedor = None
            empatados = []

        elif total_votos_candidatos == 0:
            situacao = "Sem votos válidos"
            vencedor = None
            empatados = []

        else:
            maior_quantidade_votos = max(
                candidato["votos"] 
                for candidato in self.candidatos
            )

            empatados = [
                candidato 
                for candidato in self.candidatos 
                if candidato["votos"] == maior_quantidade_votos
            ]

            if len(empatados) > 1:
                situacao = "Empate"
                vencedor = None

            else:
                situacao = "Eleição finalizada"
                vencedor = empatados[0]

        eleitores_resultado = []

        for eleitor in self.eleitores:
            if eleitor["votou"]:
                situacao_eleitor = "Votou"
            
            else:
                situacao_eleitor = "Faltou"

            eleitores_resultado.append({
                "nome": eleitor["nome"],
                "titulo_eleitor": eleitor["titulo_eleitor"],
                "situacao": situacao_eleitor
            })

        total_eleitores = len(self.eleitores)

        eleitores_que_votaram = sum(
            1
            for eleitor in self.eleitores
            if eleitor["votou"]
        )

        abstencoes = (
            total_eleitores
            - eleitores_que_votaram
        )

        if total_eleitores > 0:

            percentual_comparecimento = (
                eleitores_que_votaram
                / total_eleitores
            ) * 100

            percentual_abstencoes = (
                abstencoes
                / total_eleitores
            ) * 100

        else:
            percentual_comparecimento = 0
            percentual_abstencoes = 0

        resultado = {
            "candidatos": candidatos_resultado,
            "eleitores": eleitores_resultado,

            "total_votos": total_votos,
            "votos_validos": total_votos_candidatos,
            "votos_brancos": self.votos_brancos,
            "votos_nulos": self.votos_nulos,

            "percentual_nulos": percentual_nulos,

            "total_eleitores": total_eleitores,
            "eleitores_que_votaram": eleitores_que_votaram,
            "abstencoes": abstencoes,

            "percentual_comparecimento": percentual_comparecimento,
            "percentual_abstencoes": percentual_abstencoes,

            "situacao": situacao,
            "vencedor": vencedor,
            "empatados": empatados
        }

        self.eleicao_aberta = False

        return resultado