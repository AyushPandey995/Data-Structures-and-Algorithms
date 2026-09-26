def prime_num():
    prime_nos = []
    for i in range(1, 101):
        if i == 1:
            continue
        for j in range(2, i):
            if i% j == 0:
                break
        else:
            prime_nos.append(i)


    print(prime_nos)
prime_num()

