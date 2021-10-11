def printMenu():
    print("1.Determină dacă un număr dat este palindrom.")
    print("2.Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.")
    print("x. Iesire")

def is_palindrome(n):
    '''
    verifica daca un numar dat este palindrom
    :param n: numar natural
    :return:  True, daca n este palindrom sau False, in caz contrar
    '''
    oglindit = 0
    copie = n
    while copie > 0:
        oglindit = oglindit * 10 + copie % 10
        copie = copie //10
    if oglindit == n:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(3113) is True
    assert is_palindrome(57) is False
    assert is_palindrome(0) is True

def is_prime (n):
    '''
    Functia verifica daca un numar este prim sau nu
    :param n: numar intreg
    :return: True, daca numarul este prim sau False, in caz contrar
    '''
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def test_is_prime ():
    assert is_prime(7) is True
    assert is_prime(12) is False
    assert is_prime(2) is True

def is_superprime(n):
    '''
    functia verifica daca toate prefixele unui numar sunt prime
    :param n: numar natural
    :return: True, daca numarul este superprim sau False, in caz contrar
    '''
    if n < 2:
        return False
    while n > 0:
        if n < 2:
            return False
        if(is_prime(n) is False):
            return False
        n = n // 10
    return True

def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False

def main():
    test_is_prime()
    test_is_superprime()
    test_is_palindrome()
    while True:
        printMenu()
        n = int(input("Dati un numar: "))
        optiune = input('Dati optiunea: ')
        if optiune == "1":
            print (is_palindrome(n))
        elif optiune == "2":
            print (is_superprime(n))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")


main()