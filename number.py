'''This modules consists of mathematical operations on different types of numbers.'''


def odd(n):#checks odd number
    """This function helps to check whether given number is odd
        syntax :number.odd(any_num)
         example:
          >>>number.odd(9)
         True
         """

    if (n % 2 == 0):
        return False
    else:
        return True




def p_odds(n):#prints odd values

    i = 0
    while (i <= n):
        if (i % 2 != 0):
            print(i)
        i += 1
    else:
        return None


def i_odds(n1,n2):#prints odd numbers in the given intervals
    while(n1<=n2):
        if(n1%2!=0):
            print(n1)
        n1+=1
    else:
        return None



def even(n1):  # print even or not
    if (n1 % 2 == 0):
        return True
    else:
        return False





def p_evens(n):#prints even values

    i = 0
    while (i <= n):
        if (i % 2 == 0):
            print(i)
        i += 1
    else:
        return None

def i_evens(n1,n2):#prints odd numbers in the given intervals
    while(n1<=n2):
        if(n1%2==0):
            print(n1)
            if(n1==n2):
                return None
        n1+=1


def prime(n):#checks number is prime or not prime
    if (n > 1):
        for i in range(2, n):
            if (n % i == 0):
                return False
                break
        else:
            return True

    else:
        return False


def p_primes(n):
    for i in range(0, n + 1):
        if (i > 1):
            for j in range(2, i):
                if (i % j == 0):
                    break


            else:
                print(i)
        else:
            pass


def i_primes(n1,n2):
    for i in range(n1, n2 + 1):
        if (i > 1):
            for j in range(2, i):
                if (i % j == 0):
                    break

            else:
                print(i)
        else:
            None




