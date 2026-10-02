from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from Backend.banco_de_dados import candidatos


class MenuVotacao:

    @staticmethod
    def processar_voto(numero_1: str, numero_2: str, campo_informacao, foto_candidato, info_esquerda):

        if len(numero_1) != 1 or len(numero_2) != 1:
            campo_informacao.setText("")
            foto_candidato.clear()
            foto_candidato.setText("")
            info_esquerda.setText("")
            return

        numero_completo = numero_1 + numero_2
        candidato_encontrado = None


        for candidato in candidatos:
            if candidato["numero_candidato"] == numero_completo:
                candidato_encontrado = candidato
                break


        if candidato_encontrado:
            campo_informacao.setText("SEU VOTO VAI PARA:")

            texto_detalhes = (
                f"Nome: {candidato_encontrado['nome']}\n\n"
                f"Partido: {candidato_encontrado['partido']}"
            )
            info_esquerda.setText(texto_detalhes)

            caminho_imagem = str(candidato_encontrado["imagem"])
            pixmap = QPixmap(caminho_imagem)

            if not pixmap.isNull():
                foto_candidato.setPixmap(
                    pixmap.scaled(
                        foto_candidato.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                )
            else:
                foto_candidato.setText("Imagem não\nencontrada")


        else:
            campo_informacao.setText("SEU VOTO VAI PARA:")
            info_esquerda.setText("Candidato não encontrado\n\nVOTAR NULO")
            foto_candidato.clear()
            foto_candidato.setText("")