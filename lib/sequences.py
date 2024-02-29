def print_fibonacci(n):
    if n == 0:
        print('[]')
    elif n == 1:
        print('[0]')
    elif n == 2:
        print('[0, 1]')
    else:
        a, b, fib_seq = 0, 1, []
        for i in range(n):
            fib_seq.append(a)
            a, b = b, a + b
        print(fib_seq)