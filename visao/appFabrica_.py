#!/usr/bin/env python
# modeloo da Interface do aplicativo 
# Vamos Criar uma interface padrão 
# Estarei usando essa Interface montada dinamicamente em minhas aplicações
# Autor: Felipe M A B Huinka
import tkinter as tk
from visao.modelo.modeBloco.blocoFabrica import blockFabrica
from visao.modelo.modeMenu.menuFabrica import menuFabrica
from visao.modelo.modeAparencia.aparenciaFabrica import aparenciaFabrica
from controle.menu.custom.magento import magento

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
        self.logoLayout(blc.getBloco('Logo'))
        self.paginaLayout(blc.getBloco('Pagina'))
        self.topoLayout(blc.getBloco("Topo"))
        self.conteudoLayout(blc.getBloco("Conteudo"))
        self.rodapeLayout(blc.getBloco("Rodape"))
        self.bloco = blc    
     
        lyt = self.Layout()
        self.layout = lyt
        
        self.menu = self.Menubasico()

        self.app = janela

    def Menubasico(self):
        menu = menuFabrica(self.bloco.getBloco("Menu"))
        menu.addBotao("Teste Class", aparenciaFabrica )

    def BlocosBasico(self):
        blc = blockFabrica()
        blc.addBloco('Tudo',self.app,0)
        blc.addBloco("Direita",blc.getBloco('Tudo'))
        blc.addBloco("Logo",blc.getBloco('Direita'),4)
        blc.addBloco("Menu",blc.getBloco('Direita'),2)
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
        mn["width"] = 220

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
        
    def logoLayout(self,_logoInstancia):
        lg = _logoInstancia
        lg["width"] = 200
        lg["height"] = 50
        lg["background"] = "grey"
       