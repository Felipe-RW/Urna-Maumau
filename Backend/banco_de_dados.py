from pathlib import Path

base_dir=Path(__file__).resolve().parent.parent

eleicao_ativa = False
votos_brancos = 0
votos_nulos = 0
votos_registrados = []

candidatos =[
    #{"nome", numero do candidato, partido, total de votos, caminho da imagem}
    {"nome": "Machado de Assis", "numero_candidato": "10" , "partido": "Partido da Ironia (PI)", "votos": 0, "imagem": base_dir / "Imagens" / "MachadoDeAssis.jpg"},
    {"nome": "Guimarães Rosa", "numero_candidato": "20" , "partido": "Partido do Sertão (PS)", "votos": 0, "imagem": base_dir / "Imagens" / "JoaoGuimaraesRosa.jpg"},
    {"nome": "José de Alencar", "numero_candidato": "30" , "partido": "Partido dos Heróis (PH)", "votos": 0, "imagem": base_dir / "Imagens" / "JoseDeAlencar.jpg"},
    {"nome": "Graciliano Ramos", "numero_candidato": "40" , "partido": "Partido Sem Flores (PSF)", "votos": 0, "imagem": base_dir / "Imagens" / "GracilianoRamos.jpg"},
    {"nome": "Jorge Amado", "numero_candidato": "50" , "partido": "Partido do Povo (PP)", "votos": 0, "imagem": base_dir / "Imagens" / "JorgeAmado.jpg"}
]

eleitores =[
    #{"nome", titulo do eleitor, booliano}
    {"nome": "Fernanda Montenegro", "titulo_eleitor": "12" ,"votou": False},
    {"nome": "Laura Cardoso", "titulo_eleitor": "34", "votou": False},
    {"nome": "Lima Barreto", "titulo_eleitor": "56", "votou": False},
    {"nome": "Glória Menezes", "titulo_eleitor": "78", "votou": False},
    {"nome": "Tarcísio Meira", "titulo_eleitor": "90", "votou": False}
]

