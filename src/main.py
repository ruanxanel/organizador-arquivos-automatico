from pathlib import Path
from config import MAPEAMENTO

def organizar(pasta_alvo: str):
    pasta = Path(pasta_alvo)
    
    for arquivo in pasta.iterdir():
        if not arquivo.is_file():
            continue
        
        extensao = arquivo.suffix
        destino = MAPEAMENTO.get(extensao, "Outros")
        pasta_destino = pasta / destino
        
        pasta_destino.mkdir(parents=True, exist_ok=True)
        arquivo.rename(pasta_destino / arquivo.name)


if __name__ == "__main__":
    organizar("C:/Users/ruanp/Desktop/sla")