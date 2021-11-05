# Modelo da Interface do aplicativo 
# Vamos Criar uma interface padrão 
# Estarei usando essa Interface montada dinamicamente em minhas aplicações
# Autor: Felipe M A B Huinka

import tkinter as tk
from tkinter import Button, Frame, Label, font
from view.model.modeMenu.menuFactory import menuFactory


class appModel:

    app = None
    corpo = None
    pagina = None
    menu = None
    menuitem = None
    cabeca = None
    conteudo = None
    rodape = None

    def __init__(self): 
        
        #Inicio da Aplicação
        self.app = tk.Tk()
        #Inicio do Frame Corpo instaciado em corpo
        self.pgCorpo()

        #Inico do frame container do Menu
        self.pgMenu()
        #Chamada da instancia menuitem para botoes no menu
        self.menuitem = menuFactory(self.menu)
        

        #Fecha meu
        self.menu.pack(fill=tk.BOTH, side=tk.LEFT)

        #Inicio das Paginas
        self.pgPagina()

        #Fecha Paginas
        self.pagina.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        #Fecha Frame Corpo (Obs é nescessario o mainloop() na aplicação instaciada)
        self.corpo.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


    def pgCorpo(self):
        cp = Frame(self.app)
        cp["background"] = "grey"
        cp["width"] = 300
        cp["height"] = 300
        self.corpo = cp
    
    def setaTitulo(self,_titulo):
        self.app.title(_titulo)

    def pgMenu(self):
        mn = Frame(self.corpo)
        mn["background"] = "white"
        mn["width"] = 150
        self.menu = mn

    def pgPagina(self):
        pg = Frame(self.corpo)
        pg["background"] = "#cccccc"
        pg["width"] = 300
        pg["height"] = 200
        self.pagina = pg
    
