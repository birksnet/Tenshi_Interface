# Chamada Principal para a Aplicação TENSHI
# -- > Vamos Montar Nossa Aplicação
# Autor: Felipe M A B Huinka

class APP :
    APP = None
    BLOCO = None
    def __init__(self) :

        from visao.modelo.modeApp.appFabrica import appFabrica
        from modifica.aparencia.modelos.padrao import padrao
        
        self.APP = appFabrica(padrao())

        print("passei vasado ")
     

APP()