# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 20:05:32 2022

@author: user_lc4_59
"""

import requests, json

EquipeRegistrada = {
    "ID" : 159357,
    "Membros" : [ "Marcos" , "Ronaldo" , "Joao" ]
    }

response = requests.post("http://localhost/NovaEquipe", data=json.dumps(EquipeRegistrada))

EquipeRegistrada = {
    "ID" : 14567,
    "Membros" : [ "Carlos" , "Pedro" , "Joaquim" ]
    }

response = requests.post("http://localhost/NovaEquipe", data=json.dumps(EquipeRegistrada))

EquipeRegistrada = {
    "ID" : 987123,
    "Membros" : [ "Portuga" , "Leonardo" , "Jeronimo" ]
    }

response = requests.post("http://localhost/NovaEquipe", data=json.dumps(EquipeRegistrada))


LixeiraRegistradas = {
    "ID" : 154687,
    "Long" : 123,
    "Lat" : 321,
    "Tipo" : 'Organico',
    }

response = requests.post("http://localhost/NovaLixeira", data=json.dumps(LixeiraRegistradas))

LixeiraRegistradas = {
    "ID" : 546556,
    "Long" : 581,
    "Lat" : 963,
    "Tipo" : 'Metal',
    }

response = requests.post("http://localhost/NovaLixeira", data=json.dumps(LixeiraRegistradas))

LixeiraRegistradas = {
    "ID" : 268431,
    "Long" : 745,
    "Lat" : 159,
    "Tipo" : 'Organico',
    }

response = requests.post("http://localhost/NovaLixeira", data=json.dumps(LixeiraRegistradas))

AmbienteRegistrado = {
    "ID": 137,
    "endereco": {'Rua':"Rua Antonio Nunes",'Numero': 79,'Bairro': "Bairro Gertrudes"},
    "tipo": "Urbano"
}

response = requests.post("http://localhost/NovoAmbiente", data=json.dumps(AmbienteRegistrado))

AmbienteRegistrado = {
    "ID": 185,
    "endereco": {'Rua':"Rua Mato Grosso",'Numero': 89,'Bairro':"Bairro Dominic"},
    "tipo": "Rural"
}

response = requests.post("http://localhost/NovoAmbiente", data=json.dumps(AmbienteRegistrado))

print('Registrando passagem de RFID!!')

jsonObj = {
        "Data": "10/03/2022",
        "Hora": "10:11",
        "IDlix": LixeiraRegistradas['ID'],
        "Decrição": "Lixeira esvaziada"
}

response = requests.post("http://localhost/RegistrarEvento", data=json.dumps(jsonObj))
print(response.content)


print("\n Lixo jogado fora. Registrando.")

jsonObj = {
        "Data": "10/05/2022",
        "Hora": "15:26",
        "IDlix": LixeiraRegistradas['ID'],
        "Decrição": "Lixo Organico"
}

response = requests.post("http://localhost/RegistrarEvento", data=json.dumps(jsonObj))
print(response.content)


jsonObj = {
        "Data" : "10/05/2022",
        "Hora" : "15:26",
        "IDLix" : LixeiraRegistradas['ID'],
        "Valor" : 5
}

response = requests.post("http://localhost/NovoHistorico", data=json.dumps(jsonObj))
print(response.content)

jsonObj = {
        "Data": "11/03/2022",
        "Hora": "12:00",
        "IDlix": 546556,
        "Decrição": "Lixo Metalico"
}

response = requests.post("http://localhost/RegistrarEvento", data=json.dumps(jsonObj))
print(response.content)


jsonObj  = {
        "Data": "11/03/2022",
        "Hora": "12:00",
        "IDLix": 546556,
        "Valor": 3
}

response = requests.post("http://localhost/NovoHistorico", data=json.dumps(jsonObj))
print(response.content)


Eventos = requests.get("http://localhost/Eventos")
Historico = requests.get("http://localhost/Historico")
print("\n\n Eventos registrados:\n")
for i in json.loads(Eventos.content):
    print(i)

print("\n\n Historico registrados:\n")
for i in json.loads(Historico.content):
    print(i)      