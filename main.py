from operator import truediv
from pprint import pprint


#Ejercicio 1. Crea una función que obtenga el máximo de una lista de números
def ej1(n):
    max=n[0]
    for i in range(0, len(n)):
        if n[i]>max:
            max=n[i]
    return max
lista=[5,4,2,3,4,5,99,4,2,104]
#Ejercicio 2. Crea una función que obtenga la sumatoria de una lista de números
def ej2(n):
    sum=0
    for i in range(0,len(n)):
        sum+=n[i]
    return sum
#Ejercicio 3. Crea una función que dada una distancia en millas calcule su
#correspondiente en kms.
def ej3(n):
    return (n*1.609)

#Ejercicio 4. Crea una función que determina si una letra es una vocal
def ej4(n):
    n=n.lower()
    print(n)
    if n== 'a' or n=='e' or n=='i' or n=='o' or n=='u':
        return True
    else:
        return False
#Ejercicio 5. Crea una función que cuenta la cantidad de números pares de una lista de
#números.
def ej5(n):
    sum=0
    for i in range(0,len(n)):
        if n[i]%2==0:
            sum+=n[i]
    return sum
print(ej5(lista))
#Ejercicio 6. Crea una función que dados un número y un intervalo (inicio, fin) cuente la
#cantidad de múltiplos del número en dicho intervalo
def ej6(a,b,n):
    cont=0
    for i in range(a,b):
        if n%i==0:
            cont+=1
    return cont
#Ejercicio 7. Crea una función que dada la longitud de los tres lados de un triángulo
#determine si el triangulo es rectángulo 😱😱
def ej7(a,b,c):
    if(a*a)+(b*b)==(c*c):
        return True
    else:
        return False
#Ejercicio 8. Crea una función que calcule el máximo común divisor de dos números
#naturales 😱😱
def ej8(a,b):
    mcd = 1
    i = 1
    while (i<=a and i<=b):
        if (a%i==0 and b%i==0):
            mcd=i
        i+=1
    return mcd
#Ejercicio 9. Crea una función que dado un número n imprima los siguientes
#‘mosaicos’
def ej9(n):
    for i in range(1,n+1):
        print()
        for j in range(0,i):
            print(i,end=" ")
#Ejercicio 10 Rombo
def ej10(n: int):
    if n%2!=0:
        espacios=(n-1)/2
        asteriscos=1
        filas=(n+1)/2
        filas=int(filas); espacios=int(espacios)
    else:
        espacios=n/2
        asteriscos=2
        filas=n/2
        filas=int(filas); espacios=int(espacios)

    for i in range(0,filas):
        print("\t\t",end="")
        for j in range(0,espacios):
            print(" ",end="")
        for j in range(0,asteriscos):
            print("*",end="")
        print("")
        asteriscos=asteriscos+2
        espacios=espacios-1

    asteriscos=asteriscos-4
    espacios=espacios+2

    for i in range(1,filas):
        print("\t\t", end="")
        for j in range(0, espacios):
            print(" ", end="")
        for j in range(0, asteriscos):
            print("*", end="")
        print("")
        asteriscos = asteriscos - 2
        espacios = espacios + 1

ej10(9)