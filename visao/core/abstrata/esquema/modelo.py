# Estou criando uma class de esquema para controle dos blocos
# -- > aqui e nosso modelo do esquema de blocos
# Isso sera um recepiente para as informações dos blocos
# Autor: Felipe M A B Huinka

class modelo:
    
    nome = None
    pai = None
    fim = None
   
    def __init__(self, _nome, _nomePai, _fim = 1):
        self.nome = _nome
        self.pai = _nomePai
        self.fim = _fim

