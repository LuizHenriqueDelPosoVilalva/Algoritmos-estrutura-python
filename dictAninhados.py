familia = {
    "criança1": {
        "nome": "Joana",
        "ano": 2004
    },
    "criança2": {
        "nome": "Carlos",
        "ano": 2007
    },
    "criança3": {
        "nome": "Marcos",
        "ano": 2011
    }
}

familia["criança4"] = {"nome": "Marina", "ano": 1989}
print(familia)
print(familia["criança1"])

#percorrer dict aninhados

for f in familia:
    print(f)
print("-----------------------")

for f in familia:
    print(familia[f])
print("-----------------------")

for f in familia:
    print(familia[f]["nome"])
print("-----------------------")

#removendo dicionarios aninhados
del familia["criança1"]
print(familia)

familia.pop("criança2")
print(familia)