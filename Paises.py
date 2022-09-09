import pprint
paises = []
contador= 0

while contador < 6:
    contador += 1
    entrapais= input("Ingrese 6 países: ")
    paises.append(entrapais)
    print(f"Pais numero {contador}, {entrapais}")


##descartamos los duplicados
paises = set(paises)
paises= list(paises)
print(f'Lista de paises: {paises}')
paises.sort()
print(f'Lista de paises ordenados: {paises}')







print(paises)