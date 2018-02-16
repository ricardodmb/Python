import sys
# Lee x de la terminal
x = int ( input ( "Ingrese un natural: " ) )
#Implementacion de una verificacion no optima de la conjetura de Collatz
while x != 1 :
    if x % 2 == 0 :
        x = x / 2
    else :
        x = x * 3 + 1
sys.stdout.write(str(int(x)) + ", " x)
print ("La cadena regresa al 1.")
