# Ejercicio N. 3. repetitivos: En 1980 la ciudad A tenia 3.5 millones de habitantes y una rata  de crecimiento de 7% anual; y la ciudad B tenia 5 millones y una rata de crecimiento de 
# 5% anual. si el crecimiento poblacional se mantiene constante en las dos ciudades, hacer el diagrama de flujo y el programa en python que calcule e imprima en que año la poblacion de 
# la ciudad A es mayor que la de la ciudad B. 

from turtle import st


print("\n-----------------------------------------")
print("-------- Crecimiento poblacional ----------")
print("-----------------------------------------\n")

A=3500000
B=5000000
a=1980

#processing

while B>A:
    A=A+(A*0.07)
    B=B+(B*0.05)
    a=a+1

print("\nEn el año "+str(a)+" La poblacion de la ciudad A es mayor que la de la ciudad B\n")