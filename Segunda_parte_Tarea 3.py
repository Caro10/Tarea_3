palabras = int(input('Digame cuantas palabras tiene la lista')) #Primer pregunta

if palabras < 1:
    print("Imposible")
else:
    lista = []
    for i in range(palabras):
        print('Digame la palabra', str(i +1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print('La lista creada es', lista)

buscar = input("Dígame la palabra a buscar: ")
cont = 0
for i in lista:
    if i == buscar:
        cont += 1;
if cont == 0:
    print("La palabra '" + buscar + "' no aparece en la lista.")
elif cont == 1:
    print("La palabra '" + buscar + "' aparece una vez en la lista.")
else:
    print("La palabra '" + buscar + "' aparece", cont, "veces en la lista.")