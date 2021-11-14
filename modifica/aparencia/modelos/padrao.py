# Vou criar um modelo de aparencia padrao
#--> Podemos ver como criar modelos com nossos blocos 
# Autor: Felipe M A B Huinka

from visao.core.abstrata.esquema.fabrica import fabrica

class padrao :

    # Obrigatorio para modelos 
    modelo = None

    def __init__(self):
        # Instancia do modelo
        self.modelo = fabrica("padrao")
        self.criaEsquema()

    def criaEsquema(self):
        if self.modelo != None:
            md = self.modelo
            md.addBloco("Tudo","app")
            return self.modelo
    
    def getModelos(self):
        return self.modelo.modelos