#Vamos Criar os itens blocos que servirão para dimencionar a pagina
#Aqui teremos nossa basse ou modelo de Objeto
# Autor: Felipe M A B Huinka

class blocoItem:

    def __init__(self, _pai ,_nome, _fim ):
        self.blocoNome = _nome
        self.blocoPai = _pai
        if _fim == None:
            self.blocoFim = 'fill=tk.BOTH, side=tk.LEFT, expand=True'
        else:
            self.blocoFim = _fim

    def getNome(self):
        return self.blocoNome
    def getPai(self):
        return self.blocoPai
    def getFim(self):
        return self.blocoFim