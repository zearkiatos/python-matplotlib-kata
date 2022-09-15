


def menu ()->None:
    option = ''
    while (option != 0):
        print("------ Select an Option ------\n")
        print("1) Import example \n")
        print("2) Negative Image \n")
        print("3) Combine Image \n")
        print("4) Use plot \n")
        print("5) Use plot with more details \n")
        print("6) Use plot with Axel \n")
        print("7) Use plot Twins \n")
        print("0) Exit \n")

        option = int(input('Select an option please: '))

        if (option == 1):
            import importExample
        elif (option == 2):
            import negativeImage
        elif (option == 3):
            import combineImages
        elif (option == 4):
            import plots
        elif (option == 5):
            import plotCustom
        elif (option == 6):
            import plotWithAxes
        elif (option == 7):
            import plotTwins


menu()