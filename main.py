from pathlib import Path

pasta = Path('pasta_teste')

for arquivo in pasta.iterdir():
    if arquivo.is_file():
        print(f'Arquivo: {arquivo.name}')
        print(f'Extensão: {arquivo.suffix}')