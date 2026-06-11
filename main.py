from pathlib import Path

categorias = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos' : ['.pdf', '.docx', '.txt'],
    'Áudios' : ['.mp3', '.wav', '.ogg'],
    'Vídeos' : ['.mp4', '.mkv', '.mov'],
    'Planilhas' : ['.xlsx', '.csv'],
}



def obter_categoria(extensao):
    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            return categoria
    
    return 'Outros'
    

def garantir_pasta(pasta, categoria):
    caminho = pasta / categoria   
    if not caminho.exists():
        caminho.mkdir()      
        
        
def mover_arquivo(arquivo, categoria):
    pass



def organizar_arquivos(pasta):
    
    p = Path(pasta)
    for arquivo in p.iterdir():
        if arquivo.is_file():
            categoria = obter_categoria(arquivo.suffix)
            print(f'{arquivo.name} -> {categoria}')
            garantir_pasta(p, categoria)

            
organizar_arquivos('pasta_teste')

