#Palíndromos
#Haga un programa que pida al usuario una cadena de caracteres, y el programa diga si es o no un palíndromo

x = str ( input ( "Ingrese una cadena de caracteres: " ) )

palabra = x.replace (' ','')

if palabra == palabra[::-1]:
    print(x + " es un palíndromo")
else:
    print(x + " no es un palíndromo")
