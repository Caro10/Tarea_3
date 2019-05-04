
agenda_hospital = []

personas = [('Juan', 'Mora', 100103111, 65, 81118811, 'dolor'),
('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta'),
('Sofia', 'Alfaro', 32415116, 36, 51161161, 'consulta'),
('Carlos', 'Sanchez', 33411151, 15, 41655161, 'dolor'),
('Felipe', 'Perez', 12243151, 42, 65151111, 'documento'),
('Melissa', 'Alvarado', 734114144, 10, 87421312, 'dolor'),
('Pedro', 'Castro', 4372124141, 2, 99313131, 'dolor')]

agenda_hospital.extend(personas)


def imprimir_lista (lista,titulo):
    print("\n\n ", titulo)
    for it in lista:
        print(it)
    print("\n\n")

imprimir_lista(agenda_hospital,'Lista de pacientes en total: ')

print('En total llegaron', len(agenda_hospital), 'pacientes') #primer pregunta


resp = 0
for paciente in personas:
    resp += paciente.count('dolor') #segunda pregunta

print('Por dolor llegaron', resp, 'pacientes')

personas.sort(reverse=True, key=lambda paciente: paciente[3]) #tercera pregunta
imprimir_lista(personas, 'Tercera pregunta:  Edad')

mayores = 0
menores = 0

for paciente in personas: #cuarta pregunta
    if paciente[3] >= 18:
        mayores += 1
    else:
        menores += 1
print('Pacientes mayores de edad:',mayores, 'Pacientes menores de edad:',menores)
'''
Quinta pregunta Suponga que se atienden con 
orden de prioridad por gravedad de consulta, empezando por los que tienen dolor y 
luego por edad (mas viejo al joven), empezando por el adulto mayor.
Ordene la lista empenzando por los que tienen mayor prioridad.
'''



personas.sort(reverse=True,key=lambda paciente: tuple((1 if paciente[5]=="dolor" else 0, paciente[3])))

imprimir_lista(personas,'Quinta pregunta, prioridad')

muerte = list(filter(lambda p:p[5]!='dolor', personas))
muerte.sort(key=lambda paciente: paciente[3])
imprimir_lista(muerte, 'Sexta, los que quedaron vivos')
pass



pass