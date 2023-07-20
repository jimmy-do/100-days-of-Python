a = int(input("Check this number: "))


def prime_checker(n=a):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print('Prime')
    else:
        print('Not Prime')


prime_checker(a)
