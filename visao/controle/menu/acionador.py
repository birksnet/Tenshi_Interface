# Vou tentar criar uma class para acionamento dos botões 
# ------ Chama a Class passada via instancia 
# Autor: Felipe M A B Huinka

class acionador:

    urlBase = 'controle.custom'
    
    def __init__(self,_classMetodo):
        _classMetodo()