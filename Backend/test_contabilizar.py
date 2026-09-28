from PySide6.QtCore import QObject, Signal, Slot
from banco_de_dados import candidatos, eleitores
class SistemaUrna(QObject): 

    votoConfirmado = Signal(str, str)
    erroValidacao = Signal(str)

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
                
        if not candidato_escolhido:
            self.erroValidacao.emit("Número de candidato inválido!")
            return False

        candidato_escolhido["votos"] += 1
        
        # self.votoConfirmado.emit(eleitor_atual["nome"], candidato_escolhido["nome"])
        # return True

        
if __name__ == "__main__":
    print("--- INICIANDO TESTE DO SISTEMA DA URNA ---\n")

    # 1. Criamos funções para conectar aos Sinais (Signals) e ver as respostas no terminal
    def simular_sucesso(nome_eleitor, nome_candidato):
        print(f"🎉 SINAL RECEBIDO: Voto de {nome_eleitor} confirmado para {nome_candidato}!")

    def simular_erro(mensagem):
        print(f"❌ SINAL DE ERRO RECEBIDO: {mensagem}")


    # 2. Instanciamos a classe passando os dados importados lá do topo do seu arquivo
    urna = SistemaUrna(candidatos, eleitores)


    # 3. Conectamos os sinais do PySide6 às nossas funções de teste
    urna.votoConfirmado.connect(simular_sucesso)
    urna.erroValidacao.connect(simular_erro)


    # 4. Executamos os testes de votos no terminal
    print("Testando voto em um candidato válido (Número 10 - Machado de Assis):")
    # Nota: Como as linhas do 'votoConfirmado' estão comentadas na sua pergunta,
    # este primeiro teste apenas rodará o código internamente. 
    # Se você tirar o '#' delas na sua classe, o sinal 'simular_sucesso' será disparado.
    urna.contabilizarVoto(10) 
    print(f"Total de votos do Machado de Assis agora: {candidatos[0]['votos']}\n")


    print("Testando voto em um número inválido (Número 99):")
    # Este teste vai disparar o sinal 'erroValidacao' e mostrar a mensagem na tela
    urna.contabilizarVoto(99) 
    
    print("\n--- FIM DOS TESTES ---")
