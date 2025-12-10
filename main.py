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
    
alpha = 89
beta = 69
n = 90
print(chiffrer(demander_message(), alpha, beta, n))