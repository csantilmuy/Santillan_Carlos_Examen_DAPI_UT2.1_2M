nombre = input("Introduzca su nombre completo (Nombre Apellido): ")
print(nombre[:nombre.find(" ")])

palabra = input("Introduzca una palabra: ")
vocal = input("Introduzca una vocal: ")
print(palabra.replace(vocal,vocal.upper()))