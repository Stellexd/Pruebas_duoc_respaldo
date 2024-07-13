import random
import csv
import math

trabajadores = ["Alejandro Gómez", "Sofía Jiménez", "Javier Ramírez", "Lucía Castillo", "Daniel Moreno", "Valeria Ortiz", "Andrés Soto", "Camila Vargas", "Emilio Flores", "Natalia Reyes"]
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
    print("Sueldos menores a $800.000")
    for empleado, sueldo in menores_800:
        print(f"{empleado}su sueldo es: {sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    for empleado, sueldo in entre_800_2mill:
        print(f"{empleado} su sueldo es: {sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    for empleado, sueldo in mayores_2mill:
        print(f"{empleado}su sueldo es:{sueldo}")
        
            
def ver_sueldos():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio_sueldo=sum(sueldos) / len(sueldos)
    media_geometrica = math.prod(sueldos) **(1/len(sueldos))
    print(f"sueldo mas alto: {sueldo_max}, sueldo bajo: {sueldo_min}, sueldo promedio: {promedio_sueldo}, media geometrica:4 {media_geometrica}")
def reporte_de_sueldos():
    descuentos =[]
    for sueldo in sueldos:
        salud = sueldo*0.07
        afp = sueldo *0.12
        suel_liquido = sueldo -salud -afp
        descuentos.append((sueldo,salud, afp, sueldo))
        
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nombre', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writeheader()
        for i, desc in enumerate(descuentos):
            writer.writerow({'Nombre': trabajadores[i], 'Sueldo Base': desc[0], 'Descuento Salud': desc[1], 'Descuento AFP': desc[2], 'Sueldo Líquido': desc[3]})

        print("se genero reporte_sueldos.csv")
    
def salir():
    exit()
def menu():
    while True:
        print("\nMenu \n1.asignar sueldos aleatorios\n2.clasificar sueldos\n3.ver estadistica\n4.reporte de sueldo\n5.salir")
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
        else:
            print("no valido")
            continue
if __name__ == "__main__":
    menu()