import math
import sys

def is_prime(n):
    """
    Returns True if the given integer n is prime and False otherwise
    """
    if n <= 1:
        return False
    lim_test = math.floor(math.sqrt(n))
    x = 2
    while x <= lim_test:
        if n % x == 0:
            return False
        x += 1
    return True

if __name__ == "__main__":
    input_n = input("Digite o número a ser testado: ")
    try:
        n = int(input_n)
    except:
        print("Entrada inválida.")
        sys.exit()
    print("É primo: ", is_prime(n))
    