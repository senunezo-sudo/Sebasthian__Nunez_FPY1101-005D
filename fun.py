import os

def limpiar_pantalla():
    entrada=input("Presione Enter.")
    if entrada == "":
        os.system("cls")

def validar_entero(min,max,texto):
    while True:
        try:
            numero=int(input(texto))
            if min<=numero<=max:
                return numero
            else:
                print(f"numero fuera del rango {min}-{max}")
        except:
            print("ingrese solo valores numericos de tipo entero")

def validar_decimal(min,max,texto):
    while True:
        try:
            numero=float(input(texto))
            if min<=numero<=max:
                return numero
            else:
                print(f"numero fuera del rango {min}-{max}")
        except:
            print("ingrese solo valores numericos de tipo entero")

def validar_texto(texto):
  while True:
      try:
          entrada=input(texto)
          int(entrada)
          print("ingrese solo texto.")
      except ValueError:
          return entrada
          

def leer_opcion():
    opc=validar_entero(1,6,"""
========== MENÚ PRINCIPAL ==========
1. Cupos por género
2. Búsqueda de películas por rango de precio
3. Actualizar precio de película
4. Agregar película
5. Eliminar película
6. Salir
=====================================
""")
    return opc

def agregar_pelicula(lista):
    tresd=False
    codigo=validar_texto("ingrese el codigo de la pelicula.").upper()
    nombre=validar_texto("ingrese su nombre.").lower()
    genero=validar_texto("ingrese el genero de la pelicula. ")
    duracion=validar_entero(1,200,"ingrese la duracion de la pelicula en minutos.")
    clasificacion=validar_texto("ingrese la clasificaicon(A,B,C).").upper()
    idioma=validar_texto("ingrese el idioma de le pelicula(español/ingles).").lower
    precio=validar_entero(1,20000,"ingrese el precio.")
    cupos=validar_entero(0,50,"ingrese cupos. ")
    pregunta=validar_texto("esta en 3d(s/n)")
    if pregunta=="s":
        tresd=True
    if pregunta =="n":
        tresd=False
    print("prcesp exitoso.")
    return {'codigo': codigo,'nombre':nombre,'genero':genero,'duracion':duracion,'clasificacion':clasificacion,'idioma':idioma,'3d':tresd,'precio':precio,'cupos':cupos}
 

def cupos_genero(lista1):
      entrada=validar_texto("ingrese el genero que desea buscar. ").lower()
      limpiar_pantalla()
      for x in lista1:
         if entrada==x['genero']:
             print(f"""El total de cupos disponibles es {x['cupos']}
-----------------------------------------------------------------------
""")
        
             
        

def busqueda_precio(lista):
    minimo=validar_entero(1,20000,"ingrese el minimo.")
    maximo=validar_entero(1,20000,"ingrese el maximo.")
    limpiar_pantalla()

    for x in lista:
        if minimo<= x['precio'] <=maximo and x['cupos']>0:
            print("pelicula/s disponible/s")
            print(f"codigo:{x['codigo']}")
            print(f"pelicula: {x['nombre']}")
            print(f"precio: {x['precio']}")
            print(f"cupos disponibles: {x['cupos']}")
            print("-----------------------------------")
            
def buscar_codigo(lista):
    entrada=validar_texto("ingrese el codigo. ").upper()
    entrada2=validar_entero(1,20000,"ingrese e nuevo precio. ")

    for x in lista:
        if entrada==x['codigo']:
            x['precio']=entrada2
            print("cambio exitoso.")

def eliminar_pelicula(lista):
    entrada=validar_texto("ingrese el codigo.").upper()
    for x in lista:
        if entrada==x['codigo']:
         x=None
         print(x)
        
        