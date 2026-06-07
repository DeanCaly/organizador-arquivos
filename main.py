from pathlib import Path

categorias = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos' : ['.pdf', '.docx', '.txt'],
    'Áudios' : ['.mp3', '.wav', '.ogg'],
    'Vídeos' : ['.mp4', '.mkv', '.mov'],
    'Planilhas' : ['.xlsx', '.csv'],
}

def mover_arquivo():
    pass

def obter_categoria(extensao):
    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            return categoria
    
    return 'Outros'
    

def listar_arquivos(pasta):
    
    p = Path(pasta)
    for arquivo in p.iterdir():
        if arquivo.is_file():
            catergoria = obter_categoria(arquivo.name, arquivo.suffix)
            print(f'{arquivo.name} - {catergoria}')

            
listar_arquivos('pasta_teste')

