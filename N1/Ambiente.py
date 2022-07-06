class Ambiente:

    #construtor
    def __init__(self):
        self.ambientes = []

    def insereAmb(self, ambiente):
        self.ambientes.append(ambiente)

    def retornaAmbs(self):
        return self.ambientes

    def retornaAmb(self, ID):
        for a in self.ambientes:
            if a['ID'] == int(ID):
                return a

    def atualizaAmb(self, ambiente):

        for a in self.ambientes:
            if a['ID'] == int(ambiente['ID']):
                a['endereco'] = ambiente['endereco']
                a['tipo'] = ambiente['tipo']

    def removeAmb(self, ID):

        for a in self.ambientes:
            if a['ID'] == int(ID):
                self.ambientes.remove(a)
                break