# essa é nossa fabrica onde criaremos o modelo de TEMPLANTE
# -- > aqui e nosso modelo do esquema de blocos
# Aqui vamos usar nosso modelo e trabalhar com suas informaçoes
# Autor: Felipe M A B Huinka


class fabrica :
    modelo = None
    nome = None
    modelos = {}

    def __init__(self,_nome):
        self.nome = _nome
        from visao.core.abstrata.esquema.modelo import modelo
        self.modelo = modelo
        self.modelos = {}

    def addBloco(self, _chaveBloco, _nomePai, _finalBloco=1):
        if self.vereficaChave(_chaveBloco):
            print("ERRO! Essa chave de bloco ja existe tente outra")
        else:
            blc = self.modelo(_chaveBloco, _nomePai, _finalBloco)
            self.modelos.update({_chaveBloco:blc})

    def vereficaChave(self,_chave):
        for k, v in self.modelos.items():
            if k == _chave:
                
                return True

        return False
    