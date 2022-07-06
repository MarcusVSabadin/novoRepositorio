class Lixeira:
    
    #construtor
    def __init__(self):
        self.Lixeiras = []
        
    def insereLixeira(self, Lixeira):
        self.Lixeiras.append(Lixeira)
        
    def retornaLixeiras(self):
        return self.Lixeiras
    
    def retornaLixeira(self, ID):
        for a in self.Lixeiras:
            if a['ID'] == int(ID):
                return a
    
    def atualizaLixeira(self, Lixeira):
    
        for a in self.Lixeiras:
            if a['ID'] == int(Lixeira['ID']):
                a['ID'] = Lixeira['ID']
                a['long'] = Lixeira['long']
                a['lat'] = Lixeira['lat']
                a['tipo'] = Lixeira['tipo']
    
    def removeLixeira(self, ID):
        
        for a in self.Lixeiras:
            if a['ID'] == int(ID):
                self.Lixeiras.remove(a)
                break
        