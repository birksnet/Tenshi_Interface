#Construindo a aplicação primaria em Tkinter 
#Aqui vamos instaciar a janela basica
# Autor Felipe M A B Huinka

from visao.modelo.modeBloco.blocoFabrica import blockFabrica


class appFabrica:

    app = None
    titulo = None
    esquema = None
    tk = None
    aparencia = None

    ''' Aqui vamos Instanciar Nossa aplicação e seu sistema de blocos  '''
    def __init__(self,_instanciaEsquema = None,_instanciaAparencia=None,_tituloJanela='Aplicação Padrão - TENSHI',_execute=None):
        from tkinter import Tk, messagebox
        self.tk = Tk
        self.cria(_tituloJanela) #Chamada da construção TK

        if _instanciaEsquema != None:
            self.esquema = _instanciaEsquema
        
        if _instanciaAparencia != None:
            self.aparencia = _instanciaAparencia
        
        self.montagemEsquema()

        if self.aparencia == None:
            messagebox.showerror('Tenshi - Sem layout', 'Não foi iniciado nenhum modelo de aparencia')
        
        if _execute != None:
            _execute()

        self.app.mainloop()

    def cria(self,_titulo):
        self.app = self.tk()
        self.setTitulo(_titulo)

    def montagemEsquema(self):
        janela = blockFabrica()
        for k, v in self.esquema.modelo.modelos.items():
            if v.pai == "app":
                janela.addBloco(k,self.app,v.fim)
            else:
                
            print("Boco: "+v.pai+" adicionado a interface.")            

    def setTitulo(self,_tittulo):
        if self.app != None:
            self.titulo = _tittulo
            self.app.title(_tittulo)

    def getTitulo(self):
        return self.titulo

    def blocoMagico(self,_obModeloAbstrato):
        if isinstance(_obModeloAbstrato) :
            for obj in _obModeloAbstrato:
                print(obj)
        else:
            print('Erro! Bloco não instanciado.... ')
    
   
        

    
