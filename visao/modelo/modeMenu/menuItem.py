#Vamos Criar o menu da aplicação Baseada em um Objeto
#Aqui teremos nossa basse ou modeloo de Objeto
# Autor: Felipe M A B Huinka
class menuItem:

    def __init__(self,_txt = "", _aca= None):
        self.texto = _txt
        self.acao = _aca