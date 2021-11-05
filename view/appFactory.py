# Modelo da Interface do aplicativo 
# Vamos Criar uma interface padrão 
# Estarei usando essa Interface montada dinamicamente em minhas aplicações
# Autor: Felipe M A B Huinka
import tkinter as tk
from view.model.modeBloco.blocoFactory import blockFactory
from view.model.modeMenu.menuFactory import menuFactory


class criaApp:

    app = None
    bloco = None
    layout = None
    menu = None

    def __init__(self,_titulo):
        janela = tk.Tk()
        janela.title(_titulo)  
        
        blc = self.BlocosBasico()
        self.menuLayout(blc.getBloco('Menu'))
        self.paginaLayout(blc.getBloco('Pagina'))
        self.topoLayout(blc.getBloco("Topo"))
        self.conteudoLayout(blc.getBloco("Conteudo"))
        self.rodapeLayout(blc.getBloco("Rodape"))
        self.bloco = blc
     
        lyt = self.Layout()
        self.layout = lyt
        
        self.Menubasico()

        self.app = janela

    def Menubasico(self):
        menu = menuFactory(self.bloco.getBloco("Menu"))
        
        menu.addBotao("Menu Magento","apeto")
        menu.addBotao("Autor","Nome")

    def BlocosBasico(self):
        blc = blockFactory()
        blc.addBloco('Tudo',self.app,0)
        blc.addBloco("Menu",blc.getBloco('Tudo'),1)
        blc.addBloco("Pagina",blc.getBloco('Tudo'),2)
        blc.addBloco("Topo",blc.getBloco('Pagina'),4)
        blc.addBloco("Conteudo",blc.getBloco('Pagina'),2)
        blc.addBloco("Rodape",blc.getBloco('Pagina'),2)
        return blc

    def Layout(self):
      self.bloco.getBloco("Menu")["background"] = "#B5B5B5"

    def Loop(self):
        self.app.mainloop()

    def menuLayout(self,_menuInstacia):
        mn =_menuInstacia
        mn["background"] = "grey"
        mn["width"] = 200

    def paginaLayout(self,_paginaInstacia):
        pg = _paginaInstacia
        pg["background"] = "#cccccc"
        
    def topoLayout(self,_topoInstacia):
        tp = _topoInstacia
        tp["background"] = "#ccc"
        tp["height"] = 100

    def conteudoLayout(self,_conteudoInstancia):
        ct = _conteudoInstancia
        ct["background"] = "white"
        ct["height"] = 300
    def rodapeLayout(self,_rodapeInstancia):
        rp = _rodapeInstancia
        rp["background"] = "#ccc"
        rp["height"] = 70
        
