#Vamos Criar o menu da aplicação Baseada em um Objeto
#Aqui teremos a listagem LISTA -> Obj->menuItem 
#Nosso ResourceModel menuFactory ou Fabrica de Menu
# Autor: Felipe M A B Huinka

import tkinter as tk
from tkinter import Button, Frame, Label, font
from view.model.modeMenu.menuItem import menuItem
from controle.menu.acionador import acionador

class menuFactory :

    menuObj = []
    botao = []


    def __init__(self,_pai):
        self.pai = _pai

    def create(self,_btn):
          btn = Button(self.pai)
          btn["text"] = _btn.texto
          btn["command"] = lambda: acionador(_btn.acao)
          btn["width"]= 20
          btn.pack()
          self.botao.append(btn)

    def addBotao(self,_texto="",_acao=None):
        bt = menuItem(_texto,_acao)
        self.menuObj.append(bt)
        self.create(bt)

    def Teste(self):
        print("Teste")
   