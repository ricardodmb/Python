#suma elementos impares de sucesion de Fibonacci
#hasta el primer elemento superior a n
#f(10) = 1 + 1 + 3 + 5 + 13 = 23

x = int(input("Ingrese un entero: "))
def fib(n):
	a, b = 0,1
	s = 0
	while a < n:
		a, b = b, a+b
		if a%2 == 1:
			print(a, end='+')
			s += a
	print('=', s)
fib(x)