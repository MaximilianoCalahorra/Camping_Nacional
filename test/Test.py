import sys
sys.path.append("D:\\Curso POO Python\\Camping Nacional\\modelo")

import datetime

from CampingNacional import CampingNacional

#Test:
camping_nacional = CampingNacional()

#Test 1:
print("Test 1:")
camping_nacional.agregar_persona("Sergio", "López", 11111111)
camping_nacional.agregar_persona("Juan", "Rodríguez", 22222222)
camping_nacional.agregar_persona("María", "Fernández", 33333333)
camping_nacional.agregar_persona("Juan", "Vázquez", 44444444)
camping_nacional.agregar_persona("Ana", "Martínez", 55555555)
print("Lista de personas:")
for persona in camping_nacional.get_lst_personas():
    print(persona)
    
#Test 2:
print("Test 2:")
camping_nacional.agregar_recreo("7358902", datetime.date(2022, 9, 2), False, camping_nacional.traer_persona(11111111), 5, 300.0)
camping_nacional.agregar_campamento("6573540", datetime.date(2022, 9, 3), False, camping_nacional.traer_persona(22222222), datetime.date(2022, 9, 3), 1, 1500.0)
camping_nacional.agregar_recreo("3571398", datetime.date(2022, 9, 3), False, camping_nacional.traer_persona(33333333), 10, 300.0)
camping_nacional.agregar_campamento("2583941", datetime.date(2022, 9, 3), True, camping_nacional.traer_persona(44444444), datetime.date(2022, 9, 8), 2, 1500.0)
camping_nacional.agregar_recreo("5243925", datetime.date(2022, 9, 3), True, camping_nacional.traer_persona(55555555), 8, 300.0)
print("Lista de servicios:")
for servicio in camping_nacional.get_lst_servicios():
    print(servicio)
    
#Test 3:
print("Test 3:")
servicios = camping_nacional.traer_servicios_por_precio_final(1000)
print("Servicios con checkout y precio final mayor o igual a $1000:")
for servicio in servicios:
    print(servicio)
    
#Test 4:
print("Test 4:")
campamentos = camping_nacional.traer_campamentos_por_dias(5)
print("Campamentos con 5 o más días en el predio:")
for campamento in campamentos:
    print(campamento)