# Nossa Fabrica para os modeloos 
# ------ E aqui que a magia acontece rsrsrs
# Autor: Felipe M A B Huinka
from tkinter.constants import SEL
from visao.modelo.modeBloco.blocoFabrica import *

class aparenciaFabrica:

    aparenciaLista = { }
    pai = None
    bloco = None

    ''' Cria a class de aparencia que usa uma insatancia da class blocoFabrica '''
    def __init__(self,_appIntancia):
       print("Iniciando Temas:")
       self.pai = _appIntancia

    def padrao(self):
        pd = blockFabrica()
        pd.addBloco()

    def execute(self,str_exe):
        return 