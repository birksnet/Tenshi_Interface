#Vamos criar as listas de blocos e recursos para eles
#Aqui teremos nossa fabrica e adiministração de blocos
# Autor: Felipe M A B Huinka
from tkinter import Frame
import tkinter as tk
from view.model.modeBloco.blocoItem import blocoItem

class blockFactory:

    blocoList = {}
    blocoBase = []

    def __init__(self):
        self.blocoList = {}
        self.blocoBase = []
        

    def create(self,_bolcoObj):
        bloc = _bolcoObj
        fr = Frame(bloc.getPai())
        fr["height"] = 200
        fr["width"] = 400
        self.blocoFim(fr,bloc.getFim())
        self.blocoList.update({str(bloc.getNome()):fr})
  

    def addBloco(self,_blocoKey,_blocoPai,_blocoFim=1):
        if self.coparaKey(_blocoKey) :
            print("ERRO ! = a Key de seu bloco Já existe")
        else:
            
            blc = blocoItem(_blocoPai,_blocoKey,_blocoFim)
            self.create(blc)
            self.blocoBase.append(blc)
           
            

    def coparaKey(self,_key):
        if len(self.blocoBase) < 1:
            return False
        for bItem in self.blocoBase:
            if bItem.blocoNome == _key :
                return True
            else:
                return False

    def blocoFim(self,_ref,_opcao):
        if _opcao == 0:
            _ref.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        if _opcao == 1:
            _ref.pack(fill=tk.BOTH, side=tk.LEFT)
        if _opcao == 2:
            _ref.pack(fill='both', expand=True)
        if _opcao == 3:
            _ref.pack()
        if _opcao == 4:
            _ref.pack(fill='x')
        
        
        

    def getBloco(self,_blocoKey):
        return self.blocoList[_blocoKey]
    



