import os
import msvcrt
import csv

#Función para crear titulos
def titulo(texto : str):
    print(f"\033[33m🔰 {texto.upper()} 🔰\033[0m")

def error(texto : str):
    print(f"\033[31m❌ {texto.upper()} 💢\033[0m")

def exito(texto : str):
    print(f"\033[32m✅ {texto.upper()} 💚\033[0m")
#Tuplas - Clases
clases = [
    ("Pesas","LUN-MIE 8:30-10:00 a.m",10),
    ("Zumba", "MAR-JUE 3:30-5.40 p.m",20),
    ("Nutrición","VIE 6:00-7:30 a.m",2),
    ("Crossfit","SAB 11:30-12:55 p.m",10)
]
#Diccionario - Usuarios
usuarios = {}
#Lista - Reservas
reservas = []
#Contador para el id de usuario
numero_usuario = 100

#Comenzamos sistema
while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")

    print("""\033[32m
    Sistema gestión FitLife 🏋️‍♀️
    ══════════════════════════\033[0m
    1) Registrar Usuario
    2) Reservar clase
    3) Consultar clases disponibles
    4) Consultar clases de usuario
    5) Consultar usuarios
    0) Salir
    \033[32m══════════════════════════\033[0m""")
    opcion = input("Seleccione : ")
    if opcion=="0":
        titulo("Adios")
        break
    elif opcion=="1":
        titulo("Registrar Usuario")
        nombre = input("Ingrese nombre de usuario : ").title()
        #Validar que nombre de usuario no se repita
        if nombre not in usuarios.values(): #values solo captura el valor no las llaves
            usuarios[numero_usuario] = nombre
            exito(f"Usuario {numero_usuario} Registrado")
            numero_usuario+=100
        else:
            error("Usuario ya registrado")
    elif opcion=="2":
        titulo("Reservar Clase")
        codigo = int(input("Ingrese código de usuario : "))
        if codigo in usuarios:
            curso = input("Ingrese curso para inscribir : ").capitalize()
            centinelaCurso = False
            centinelaCupos = False
            for c in clases:
                if c[0].capitalize() == curso:
                    centinelaCurso = True
                    if c[2]>0: #Verificamos si hay cupos
                        centinelaCupos = True
                        #Realizar la reserva
                        reservas.append([codigo, usuarios[codigo],c[0],c[1]])
                        exito("Reserva realizada")
                        #Descontar cupo
                        actualizacionCupo = (c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacionCupo)
                        #Registrar reservas en csv
                        with open('reporte_reservas.csv','w',newline='', encoding='utf-8') as a:
                            escribir = csv.writer(a, delimiter=",")
                            escribir.writerows(reservas)
                        break
            if centinelaCurso==False:
                error("No existe el curso")
            if centinelaCupos==False:
                error("Cupos no disponible")
        else:
            error("Código no existe")
    elif opcion=="3":
        titulo("Consultar clases disponibles")
        for c in clases:
            print(f"{c[0]} Horario: {c[1]} Cupos: {c[2]}")
    elif opcion=="4":
        titulo("Consultar reservas de usuarios")
        if len(reservas)>0:
            codigo = int(input("Ingrese código de usuario : "))
            centinela = False
            for r in reservas:
                if r[0]==codigo:
                    print(f"{r[0]} {r[1]} Curso: {r[2]} Horario: {r[3]}")
                    centinela=True
            if centinela == False:
                error("El código no tiene reservas asociadas")
        else:
            error("No existen reservas")
    elif opcion=="5":
        titulo("Listado Usuarios")
        if len(usuarios)>0:
            for u in usuarios:
                print(f"{u} : {usuarios[u]}")
        else:
            error("No hay usuarios registrados")
    else:
        error("Opción no valida")
