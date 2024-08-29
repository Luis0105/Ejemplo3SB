n = int(input("¿Cuántos valores quieres?: " ))
a = 0
b = 1
print(a)
print(b)
for i in range(n):
    aux = a + b   # Usamos una variable auxiliar para obtener el siguiente valor de la serie
    print(aux)
    a = b
    b = aux