## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(n):
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	## DEFINIR FUNCION PARA CONTAR DIVISORES
	def get_divisors_count(n):
		count = 0
		i = 1
		while i <= n:
			if n % i == 0:
				count += 1
			i += 1
		return count 
	## DEFINIR FUNCIÓN PARA DETERMINAR SI ES ANT-PRIME
	def is_antiprime(n):
		if n == 1:
			return True 
		divisors_count = get_divisors_count(n)
		i = 1
		while i < n:
			if get_divisors_count(i) >= divisors_count:
				return False
			i += 1
		return True
	##DEFINIR LA FUNCIÓN PRINCIPAL
	def main(n):
		if is_antiprime(n):
			return "anti-prime"
		else:
			return "not anti-prime"
	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"

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
