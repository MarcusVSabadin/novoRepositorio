# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 20:10:24 2022

@author: user_lc4_59
"""


class Equipe:

    # construtor
    def __init__(self):
        self.Equipes = []

    def insereEquipe(self, Equipe):
        self.Equipes.append(Equipe)

    def retornaEquipes(self):
        return self.Equipes

    def retornaEquipe(self, ID):
        for a in self.Equipes:
            if a['ID'] == int(ID):
                return a

    def atualizaEquipe(self, Equipe):

        for a in self.Equipes:
            if a['ID'] == int(Equipe['ID']):
                a['ID'] = Equipe['ID']
                a['Membros'] = Equipe['Membros']

    def removeEquipe(self, ID):

        for a in self.Equipes:
            if a['ID'] == int(ID):
                self.Equipes.remove(a)
                break
