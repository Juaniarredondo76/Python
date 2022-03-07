                    #logica con python 
#edad=int(input("digita tu edad: "))
#print(edad)
                 # condicion logica siempre 
#bandera=True
#if(edad>=18 and bandera==True):
 #   print("bienvenido a la chismosa")

                    #EJERCICIO NUMERO 1

'''
#else:
  #  print ("devuelvase...")
#nivelAgua=int(input("digite el nievel de agua "))
#if(nivelAgua<200):
 #   print("la represa tien poca agua ")
#elif(nivelAgua>=200 and nivelAgua<450):
 #   print("la represa esta fool ")
#elif(nivelAgua>=450):
 #   print("cuidado, abra compuertas ")
#else:
 #print("digito un nivel invalido de agua ")
 '''

                                #JUAGANDO CON EL EJERCICIO NUMERO 1

'''nivelAgua=float(input("digite el nievel de agua "))
if(nivelAgua>0 and <200):
   print("la represa tien poca agua ")
elif(nivelAgua>=200 and nivelAgua<450):
   print("la represa esta fool ")
elif(nivelAgua>=450):
  # print("cuidado, abra compuertas ")
else:
    print("digito un nivel invalido de agua ") 
'''

                                #EJERCICIO NUMERO 2

'''import string

mes=string(input("Digite la estacion del año  ").lower())

if(mes=='enero' or mes=='febrero' or mes=='marzo' ):
    print("estamos en invierno ")
elif(mes=='Abril' or mes=='mayo' or mes=='junio'):
    print("estamos en verano ")
elif(mes=='julio' or mes=='agosto' or mes=='septiempre'):
    print("estamos en Otoño")
elif(mes=='octubre' or mes=='noviembre' or mes=='Diciembre'):
    print("estamos en primavera ")
else:
    print("digita un mes valido")
'''

                                #EJERCICIO NUMERO 3 EDAD 

'''
edad=float(input("Digite el edad: "))
if(edad>=0 and edad<=14):
    print("la estapa de la vida es la que te encuentras es: NIÑO ")
elif(edad>14 and edad<=28):
    print("la estapa de la vida es la que te encuentras es: JOVEN")
elif(edad>28 and edad<60):
    print("la estapa de la vida es la que te encuentras es: ADULTO")
elif(edad>=60):
    print("la estapa de la vida es la que te encuentras es: ADULTO MAYOR")
else:
    print("error al digitar la edad: ")
'''

                                #EJEMPLO NUMERO 4 OPERADOR TERNARIO

parametro=True
print("El para mtro es verdadero")if parametro==True else print("El parametro es falso")

