import random
import csv
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []

def asignar_sueldo_random():
    global sueldos
    sueldos =[random.randint(300000, 2500000) for _ in trabajadores]
    print("sueldo asignado aleatoriamente correctamente")
    
    
    
def clasificar_sueldos():
    menores_800=[]
    entre_800_2mill= []
    mayores_2mill= []
    
    for i, sueldo in enumerate (sueldos):
        if sueldo < 800000:
            menores_800.append((trabajadores[i], sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800_2mill.append((trabajadores[i], sueldo))
        else:
            mayores_2mill.append((trabajadores[i],sueldo))
            
def ver_sueldos():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio_sueldo=sum(sueldos) / len(sueldos)
    media_geometrica = math.prod(sueldos) **(1/len(sueldos))
def reporte_de_sueldos():
    
def salir():

def menu():
    while True:
        print("menu \n1.asignar sueldos aleatorios\n2.clasificar sueldos\n3.ver estadistica\n4.reporte de sueldo\n5.salir")
        opc= int(input())
        
        if opc == 1:
            asignar_sueldo_random()
        elif opc == 2:
            clasificar_sueldos()
        elif opc == 3:
            ver_sueldos()
        elif opc ==4:
            reporte_de_sueldos()
        elif opc == 5:
            salir()    
        
menu()        
        