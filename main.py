from pathlib import Path

categorias = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos' : ['.pdf', '.docx', '.txt'],
    'Áudios' : ['.mp3', '.wav', '.ogg'],
    'Vídeos' : ['.mp4', '.mkv', '.mov'],
    'Planilhas' : ['.xlsx', '.csv'],
}

def garantir_pasta(pasta, categoria):
    for p in pasta.iterdir():
        if p.name == categoria:
            print('pasta encontrada')
        else: 
            return 'Não encontrei a pasta'
    
    
def mover_arquivo(arquivo, categoria):
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
            categoria = obter_categoria(arquivo.suffix)
            print(f'{arquivo.name} -> {categoria}')
            garantir_pasta(p, categoria)

            
listar_arquivos('pasta_teste')

