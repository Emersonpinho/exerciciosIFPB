lista = [10,30,50,60,31,43,53,65,1,3,4,6,8]

lista_filtrada = list( filter(lambda numero: numero > 30, lista) )

print(lista_filtrada)