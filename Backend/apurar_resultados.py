class ApurarResultado:
    # aqui esta recebendo os dados da eleicao
    def __init__(
        self,
        candidatos,
        eleitores,
        votos_brancos,
        votos_nulos,
        eleicao_aberta
    ):
        self.candidatos = candidatos
        self.eleitores = eleitores
        self.votos_brancos = votos_brancos
        self.votos_nulos = votos_nulos
        self.eleicao_aberta = eleicao_aberta


    # aqui faz a apuracao dos resultados
    def apurarResultado(self):

        # aqui verifica se a eleicao esta aberta
        if not self.eleicao_aberta:
            return None

        # aqui soma os votos dos candidatos
        total_votos_candidatos = sum(
            candidato["votos"]
            for candidato in self.candidatos
        )

        # aqui soma todos os votos
        total_votos = (
            total_votos_candidatos
            + self.votos_brancos
            + self.votos_nulos
        )

        # aqui calcula a porcentagem de votos nulos
        if total_votos > 0:
            percentual_nulos = (
                self.votos_nulos / total_votos
            ) * 100
        else:
            percentual_nulos = 0

        # aqui verifica se a eleicao foi anulada
        if percentual_nulos > 50:
            situacao = "Eleição anulada"
            vencedor = None
            empatados = []

        # aqui verifica se não teve votos válidos
        elif total_votos_candidatos == 0:
            situacao = "Sem votos válidos"
            vencedor = None
            empatados = []

        else:
            # aqui encontra a maior quantidade de votos
            maior_quantidade_votos = max(
                candidato["votos"]
                for candidato in self.candidatos
            )

            # aqui encontra os candidatos com mais votos
            empatados = [
                candidato
                for candidato in self.candidatos
                if candidato["votos"] == maior_quantidade_votos
            ]

            # aqui verifica se houve empate
            if len(empatados) > 1:
                situacao = "Empate"
                vencedor = None

            # aqui define o vencedor
            else:
                situacao = "Eleição finalizada"
                vencedor = empatados[0]

        # aqui guarda o resultado final
        resultado = {
            "candidatos": self.candidatos,
            "eleitores": self.eleitores,
            "votos_brancos": self.votos_brancos,
            "votos_nulos": self.votos_nulos,
            "situacao": situacao,
            "vencedor": vencedor,
            "empatados": empatados
        }

        # aqui encerra a eleição
        self.eleicao_aberta = False

        # retorna o resultado
        return resultado