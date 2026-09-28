from PySide6.QWidgets import QMessageBox

def apurarResultados(candidatos, eleitores, votos_brancos, votos_nulos, urna_encerrada):
    if urna_encerrada:
        QMessageBox.warnin(None, "Urna encerrada", "A eleição já foi encerrada.")
        return None

    resposta = QMessageBox.question(None, "Finalizar eleição", "Deseja realmente finalizar a eleição ?", QmessageBox 
.Yes | QMessageBox.No)

if resposta != QMessageBox.Yes:
    return None

total_validos = 0

for candidato in candidatod:
    total_valido += canditado.quantidade_de_votos

total_votos = total_vailidos + votos_brancos + votos_nulos

