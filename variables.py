
nombre= "Osiris"
apellido= "Rivera"
edad= 26
estatura= 1.59
estudiante= True

print(f"Hola mi nombre es {nombre} {apellido}",f"tengo {edad} años",f"Mido {estatura}m",F"y mi estatus de estudiante es {estudiante}")

#  límite de los enteros y los flotantes en python
'''
Python tiene enteros sin límite y los floats tienen un limite 
de 64 bits por lo que el número más grande sería 1.8 * 10^308
'''


n = int(input("Introduce un número par: "))
suma = n * (n + 1)
print("La suma de los primeros números pares desde 1 hasta " + str(n) + " es " + str(suma))