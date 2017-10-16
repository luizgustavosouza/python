cidades = [["61","Brasilia"],["71","Salvador"],["11","Sao Paulo"],["21","Rio de Janeiro"],["32","Juiz de Fora"],["19","Campinas"],["27","Vitoria"],["31","Belo Horizonte"]]

busca = input()
for i in range(len(cidades)):
    i += 1
    for j in range(len(cidades[i])):
        j += 1
        print(cidades[i][j])
