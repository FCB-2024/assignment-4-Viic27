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

# Manejo de argumentos de línea de comandos
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"error: {sys.argv[0]} <number>")
    else:
        number = int(sys.argv[1])
        result = main(number)
        print(result)
