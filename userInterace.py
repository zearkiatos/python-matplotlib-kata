


def menu ()->None:
    option = ''
    while (option != 0):
        print("-----Select an Option ------\n")
        print("1) Import example \n")
        print("2) Negative Image \n")
        print("3) Combine Image \n")
        print("0) Exit \n")

        option = int(input('Select an option please: '))

        if (option == 1):
            import importExample
        elif (option == 2):
            import negativeImage as negativeImage
        elif (option == 3):
            import combineImages as combineImages


menu()