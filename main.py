def demander_message():
    message = input("Enter message: ")

    # mauvais_message = True
    # while mauvais_message == True:
    #     mauvais_message = True
    #     for lettre in message:
    #         if ord(lettre) < 32 or ord(lettre) > 122:
    #             print ("mauvais message")
    #             mauvais_message = True

    return message

print(demander_message())