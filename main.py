def is_palindrome(n):
    '''
    determina daca un numar este palindrom
    :param n: nr care se verifica
    :return: 
    '''
    palindrom = 0
    copie_n = n
    while n:
       palindrom = n % 10 * 10 + palindrom
       n //=10
    if palindrom == copie_n:
        return True
    else:
        return False

def test_is_palindrome():
    assert (1855) == False
    assert (1331) == True

def main():
    n = int(input("Dati un numar: "))

main()