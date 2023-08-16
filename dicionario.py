disciplina = {
    "nome": "Progr. de compotadores",
    "semestre": 2,
    "cargaHoraria": 105,
    "curso": "TADS",
    "emOferecimento": True
}

#adicionando
disciplina["ano"] = 2023

#atualizando
disciplina["nome"] = "Linguagem de Programação"

#romevendo através da chave
disciplina.pop("curso")
print(disciplina)

#removendo a ultima dupla(chave/valor)
disciplina.popitem()
print(disciplina)

print("--Diciplina--")
print("Nome : ",disciplina["nome"])
print("Carga horária: ",disciplina["cargaHoraria"])
print("Semestre: ", disciplina["semestre"])
print("Nome: ", disciplina["nome"])
print("Ano: ", disciplina["ano"])

#funções aplicaveis
print("tamanho do dicionario ", len(disciplina))

print(disciplina.get("ano", "Não econtrado"))
print(disciplina.get("nome", "Não encontrado"))

#chaves e valores
x = disciplina.keys()
y = disciplina.values()
print(x,y)

#dict para tuplas
tuples = disciplina.items()
print(tuples)

#percorrendo o dicionario
#imprime as chaves
for d in disciplina:
    print(d)

#imprime os valores nas posições de cada chave
for d in disciplina:
    print(disciplina[d])