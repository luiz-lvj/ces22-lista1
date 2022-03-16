import sys
def sum_to(n):
    """ 
    Returns the sum of all integer numbers up to and including n. 
    If n is not an integer or n < 0, the return is 0.
    """
    if type(n) != int or n < 0: 
        print("Entrada inválida.")
        sys.exit()
    return int(n*(n+1)/2)

if __name__ == "__main__":
    input_n = 0
    try:
        input_n = int(input("Insira o número de entrada: "))
    except:
        print("Entrada inválida.")
        sys.exit()
    ans = sum_to(input_n)
    print("Soma:  ", ans)