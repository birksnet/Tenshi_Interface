# Estou criando uma class de modelo para controle da aparencia
# -- > aqui onde vamos montar a aparencia dos blocos 
# Autor: Felipe M A B Huinka



class modelo:

    #chave da referencia e tipo do componente da referencia Exemplo: bloco > campo > titulo > texto
    nome = None
    componente = None

    atributos = {}

    def __init__(self,_nomeAparencia,_componente='bloco'):
        self.componente = _componente
        self.nome = _nomeAparencia

    def addAtributo(self,_chaveAtributo,_valorAtributo=None):
        if _chaveAtributo == None or _chaveAtributo == '':
            print("Erro! - Atribua a chave para modelo de aparencia")
            return False
        if self.igual(_chaveAtributo):
            print("Esse atributo ja existe! tente outro ou modifique esse ")
            return False

        self.atributos.update({self.vChave(_chaveAtributo):_valorAtributo})
     

    def getAtributo(self,_chaveAtributo):
        if self.vChave(_chaveAtributo) != None:
            return self.atributos[self.vChave(_chaveAtributo)]
        else:
            print("Erro! Chave de atributo não existe!")
            
    def getListaAtributos(self):
        return self.atributos

    def igual(self,_chaveAtributo):
        for kAt, vAt in self.atributos.items():
            if kAt == _chaveAtributo:
                return True
        return False

    def vChave(self,_chaveNome):
        chaveNonme = {
            #nomes para cor de fundo
            'background':'background',
            'corFundo':'background',
            'bg':'background',
            'bgColor':'background',
            #nome para larguras
            'size-x':'width',
            'width':'width',
            'largura':'width',
            'x':'width',
            #nomes para altura
            'height':'height',
            'altura':'height',
            'y':'height',
            'size-y':'height'
        }

        for k, v in chaveNonme.items():
            if k == _chaveNome:
                return v
        return None