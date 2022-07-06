# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:09:55 2022

@author: user_lc4_59
"""

from Lixeira import Lixeira
from Equipe import Equipe
from Ambiente import Ambiente
from Historico import HistSens
from Evento import Evento
import flask, json


ListaEquipes = Equipe()
ListaEventos = Evento()
ListaLixeira = Lixeira()
Registro = HistSens()
listaAmbientes = Ambiente()

app = flask.Flask(__name__)

@app.route('/Equipes')
def mostraEquipes():
    return json.dumps(ListaEquipes.retornaEquipes())
        
@app.route("/Equipe/<ID>")
def RetornaEquipe(ID):
    return json.dumps(ListaEquipes.retornaEquipe(ID))              

@app.route("/NovaEquipe", methods=["POST"])
def NovaEquipe():
    new = flask.request.data
    ListaEquipes.insereEquipe(json.loads(new))
    msg = "Equipe adicionada!!"
    return json.dumps({'mensagem': msg})

@app.route("/attEquipe", methods=["PUT"])
def atualizaEquipe():
    new = flask.request.data
    ListaEquipes.atualizaEquipe(json.loads(new))
    msg = 'Equipe atualizada'
    return json.dumps({'mensagem': msg })
    
@app.route("/RemoveEquipe/<ID>", methods=["DELETE"])
def removeEquipe(ID):
    ListaEquipes.removeEquipe(ID)
    msg = 'Equipe ' + ID + ' removida'
    return json.dumps({'mensagem': msg})

@app.route("/RegistrarEvento", methods=["POST"])
def RegistrarEvento():
    new = flask.request.data
    ListaEventos.insereEvento(json.loads(new))
    msg = 'Evento registrado!!'
    return json.dumps({'mensagem': msg})

@app.route("/Eventos")
def mostrarEventos():
    return json.dumps(ListaEventos.retornaEventos())

@app.route("/NovaLixeira", methods=["POST"])
def NovaLixeira():
    new = flask.request.data
    ListaLixeira.insereLixeira(json.loads(new))
    msg = "Lixeira adicionada!!"
    return json.dumps({'mensagem': msg})

@app.route("/Lixeira")
def mostrarLixeiras():
    return json.dumps(ListaLixeira.retornaLixeiras())

@app.route("/Lixeira/<ID>")
def RetornaLixeira(ID):
    return json.dumps(ListaLixeira.retornaLixeira(ID))              

@app.route("/attLixeira", methods = ["Post"])
def atualizaLixeira():
    new = flask.request.data
    ListaLixeira.atualizaLixeira(json.loads(new))
    msg = 'Lixeira atualizada'
    return json.dumps({'mensagem': msg })

@app.route("/RemoveLixeira/<ID>", methods=["DELETE"])
def removeLixeira(ID):
    ListaLixeira.removeLixeira(ID)
    msg = 'Lixeira ' + ID + ' removida'
    return json.dumps({'mensagem': msg})

@app.route('/Historico')
def mostraHistorico():
    return json.dumps(Registro.retornaHistorico())

@app.route("/NovoHistorico", methods=["POST"])
def NovoHistorico():
    new = flask.request.data
    Registro.insereHistSens(json.loads(new))
    msg = "Historico adicionado!!"
    return json.dumps({'mensagem': msg})

@app.route('/Ambientes')
def mostraAmbientes():
    return json.dumps(listaAmbientes.retornaAmbs())

@app.route("/Ambientes/<ID>")
def RetornaAmbiente(ID):
    return json.dumps(listaAmbientes.retornaAmb(ID))

@app.route("/NovoAmbiente", methods=["POST"])
def NovoAmbiente():
    new = flask.request.data
    listaAmbientes.insereAmb(json.loads(new))
    msg = "Ambiente adicionada!!"
    return json.dumps({'mensagem': msg})

@app.route("/attAmbiente", methods=["PUT"])
def atualizaAmbiente():
    new = flask.request.data
    listaAmbientes.atualizaAmb(json.loads(new))
    msg = 'Ambiente atualizado'
    return json.dumps({'mensagem': msg })

@app.route("/RemoveAmbiente/<ID>", methods=["DELETE"])
def removeAmbiente(ID):
    listaAmbientes.removeAmb(ID)
    msg = 'Ambiente ' + ID + ' removido'
    return json.dumps({'mensagem': msg})
    
if __name__ == "__main__":
    Equipes = []
    app.run(port=80)