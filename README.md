# Organizador de Arquivos Automático

Script em **Python** que organiza os arquivos de uma pasta, movendo cada um para uma subpasta de acordo com a sua extensão.

O projeto tem como objetivo praticar manipulação de arquivos e pastas com o módulo `pathlib`.

---

## Sobre o projeto

O script percorre os arquivos da pasta escolhida e os move para subpastas organizadas por categoria. As subpastas são criadas automaticamente quando necessário.

Arquivos com extensões que não estão mapeadas são movidos para a pasta **Outros**.

O projeto foi desenvolvido como parte dos meus estudos em **Python e automação**.

---

## Tecnologias utilizadas

- Python 3
- Módulo `pathlib`

---

## Estrutura do projeto

```
src
├── __init__.py
├── config.py
└── main.py
```

### main.py

Contém a função `organizar`, que percorre a pasta e move os arquivos.

### config.py

Contém o dicionário `MAPEAMENTO`, que relaciona cada extensão à sua pasta de destino.

---

## Categorias

| Pasta | Extensões |
| --- | --- |
| Documentos | `.pdf`, `.docx`, `.txt` |
| Imagens | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg` |
| Videos | `.mp4`, `.mkv` |
| Áudio | `.mp3`, `.wav` |
| Compactados | `.zip`, `.rar` |
| Outros | Qualquer outra extensão |

Para incluir novas extensões ou categorias, basta editar o dicionário `MAPEAMENTO` em `config.py`.

---

## Como executar

### Pré-requisitos

- Python 3 instalado

### Passos

```bash
# Clonar o repositório
git clone https://github.com/ruanxanel/organizador-arquivos-automatico.git

# Entrar na pasta do projeto
cd organizador-arquivos-automatico/src
```

Abra o arquivo `main.py` e altere o caminho da pasta que deseja organizar no final do arquivo:

```python
if __name__ == "__main__":
    organizar("C:/caminho/da/sua/pasta")
```

Depois execute:

```bash
python main.py
```

---

## Aviso

Os arquivos são **movidos** (não copiados). Teste primeiro em uma pasta de exemplo antes de usar em pastas importantes.

---

## Conceitos praticados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Python
- Funções
- Dicionários
- Módulo `pathlib`
- Manipulação de arquivos e pastas
- Organização de código em módulos
- Automação de tarefas

---

## Objetivo

Este projeto faz parte da minha jornada de aprendizado em **programação**.

O objetivo é aplicar na prática os conceitos estudados e construir projetos para meu portfólio.

---

## Próximos passos

- [ ] Receber a pasta por argumento de linha de comando
- [ ] Tratar arquivos com o mesmo nome na pasta de destino
- [ ] Tratar extensões em maiúsculas (`.PDF`, `.JPG`), hoje enviadas para "Outros"
- [ ] Adicionar mais categorias (código, planilhas, apresentações)
- [ ] Registrar um log dos arquivos movidos
- [ ] Executar a organização automaticamente de tempos em tempos

---

## Autor

**Ruan Henrique**

Estudante de Ciência da Computação, focado em desenvolvimento Back-End com Java e Spring Boot.