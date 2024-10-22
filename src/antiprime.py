import sys
	## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
	## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
	## COMMAND LINE SPECIFIED BELOW
def main(x):
		## YOU CODE SHOULD START HERE AST THE SAME
		## IDENTATION AS THIS COMMENT
		i = 1
		sum1 = 0
		sum2 = 0
		y = x - 1
		while (i <= x):
			if (x % i == 0):
				sum1 = sum1 + 1
			i = i + 1
		while (y >= 1 and sum2 < sum1):
			i = 1
			sum2 = 0
			while (i <= y):
				if (y % i == 0):
					sum2 = sum2 + 1
				i = i + 1
			y = y - 1
		if (sum2 < sum1):
			res = "anti-prime"
		else:
			res = "not anti-prime"
	
		## THE LAST LINES OF YOUR CODE SHOULD EITHER
		## RETURN THE VALUE "anti-prime" or "not anti-prime"
		## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
		## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
		## "anti-prime" or "not anti-prime"
		return(res)

	## DO NOT REMOVE THIS LINE BELOW
		if __name__ == "__main__" :
			x = int(sys.argv[1])
			
		## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
		## TO RUN THIS PROGRAM AS, FOR INSTANCE:
		## $ python antiprime.py 6
		## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
		## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
		print(main(x))
## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(n):
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	## DEFINIR FUNCION PARA CONTAR DIVISORES
	
	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
import sys
# Función para contar los divisores de un número
def get_divisors_count(n):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count
# Función para verificar si un número es anti-prime
def is_antiprime(n):
    if n == 1:
        return True  # El 1 es considerado "anti-prime"
    
    divisors_count = get_divisors_count(n)
    i = 1
    while i < n:
        if get_divisors_count(i) >= divisors_count:
            return False
        i += 1
    return True

# Función principal que decide si un número es anti-prime
def main(n):
    if is_antiprime(n):
        return "anti-prime"
    else:
        return "not anti-prime"
## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	import sys
	if len(sys.argv) != 2:
		print(f"error: {sys.argv[0]} <number>")
	else:
		number = int(sys.argv[1])
		result = main(number)
		print(main(number))
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
