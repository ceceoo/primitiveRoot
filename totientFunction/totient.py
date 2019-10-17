while True:
    try:
        n = int(input("Please input a number"))
        break
    except ValueError:
        print("Not a valid number.")


def is_prime_with_n(n, a):
    while a != 1:
        temp = n % a
        if temp == 0:
            break
        else:
            n = a
            a = temp
    return False if a > 1 else True


def totient(n):
    definite_t = [1]
    t = list(filter(lambda a: is_prime_with_n(n, a), range(2, n)))
    print("fai(n) =", len(definite_t+t))
    print("The result of totient function is", definite_t+t)


if __name__ == "__main__":
    totient(n)