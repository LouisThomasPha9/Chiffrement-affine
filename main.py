def demander_message():
    message = input("Enter message: ")

    error = False
    for lettre in message:
            if ord(lettre) < 32 or ord(lettre) > 122:
                print ("Unknow character")
                error = True

    while error:
        error = False
        message = input("Enter message: ")

        for lettre in message:
            if ord(lettre) < 32 or ord(lettre) > 122:
                print ("Unknow character")
                error = True

    return message

def chiffrer(M, alpha, beta, n):
    C = str()
    for lettre in M:
        nb = ord(lettre)
        C += chr(((alpha*nb) + beta) % n)
    return C

def euclide_etendu(a, b):
    r1, x1, y1, r2, x2, y2 = a, 1, 0, b, 0, 1
    while r2 != 0:
        q = r1 // r2
        r1, x1, y1, r2, x2, y2 = r2, x2, y2, r1 - q*r2, x1 - q*x2, y1 - q*y2
    return r1, x1, y1
    
def déchiffrer(C, alpha, beta, n):
    M = str()
    for lettre in C:
        nb = ord(lettre)
        M += chr(((nb - beta) * euclide_etendu(alpha, beta)[2]) % n)
    return M

alpha = 89
beta = 69
n = 90
print(chiffrer(demander_message(), alpha, beta, n))
print(déchiffrer(demander_message(), alpha, beta, n))