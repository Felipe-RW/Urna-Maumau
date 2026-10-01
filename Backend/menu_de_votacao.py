from banco_de_dados import candidatos
from PySide6.QtGui import QPixmap


class MenuVotacao:

    @staticmethod
    def processar_voto(numero_1: str, numero_2: str, campo_informacao, foto_candidato):

        if len(numero_1) != 1 or len(numero_2) != 1:
            campo_informacao.setText("")
            foto_candidato.clear()
            return

        numero_completo = numero_1 + numero_2
        candidato_encontrado = None


        for candidato in candidatos:
            if candidato["numero_candidato"] == numero_completo:
                candidato_encontrado = candidato
                break

        if candidato_encontrado:

            texto = (
                f"Nome: {candidato_encontrado['nome']}\n\n"
                f"Partido: {candidato_encontrado['partido']}"
            )
            campo_informacao.setText(texto)


            caminho_imagem = str(candidato_encontrado["imagem"])
            pixmap = QPixmap(caminho_imagem)

            if not pixmap.isNull():
                foto_candidato.setPixmap(pixmap)
            else:
                foto_candidato.setText("Imagem não encontrada")
        else:

            campo_informacao.setText("\nVOTO NULO")
            foto_candidato.clear()
