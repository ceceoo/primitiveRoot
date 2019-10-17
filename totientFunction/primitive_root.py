while True:
    try:
        n = int(input("Please input a number"))
        break
    except ValueError:
        print("Not a valid number.")


# Test if the input is valid
while True:
    try:
        n = int(input("Please input a number"))
        break
    except ValueError:
        print("Not a valid number.")


# create a dictionary, put each result in it, calculate the number of elements, true if it equals n-1
def is_primitive_root(n):
    primitive_root = []
    for i in range(2, n):
        modulo_list = []
        for k in range(1, n):
            modulo_num = pow(i, k) % n
            modulo_list.append(modulo_num)
        if len(set(modulo_list)) is n-1:
            primitive_root.append(i)
    return primitive_root


print(n, "'s primitive root is", is_primitive_root(n))
