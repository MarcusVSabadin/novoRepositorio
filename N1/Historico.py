class HistSens:
    
    #construtor
    def __init__(self):
        self.Historico = []
        
    def insereHistSens(self, HistSens):
        self.Historico.append(HistSens)
        
    def retornaHistorico(self):
        return self.Historico