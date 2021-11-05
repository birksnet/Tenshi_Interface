# Vou tentar criar uma class para acionamento dos botões 

class acionador:

    urlBase = 'controle.custom'
    
    def __init__(self,_classMetodo):
        cm = _classMetodo
        print(cm)