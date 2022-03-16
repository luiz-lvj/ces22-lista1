def is_palindrome(input_str):
    """
    Returns True if the string input is a palindrome and False otherwise.
    """
    if len(input_str) == 0:
        return True
    if len(input_str) == 1:
        return True
    size = len(input_str)
    if input_str[0] != input_str[size-1]:
        return False
    new_str = input_str[1:size-1]
    return is_palindrome(new_str)

if __name__ == "__main__":
    input_str = input("Digite a string de entrada: ")
    print("É palíndromo: ", is_palindrome(input_str))