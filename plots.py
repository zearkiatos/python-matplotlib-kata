import matplotlib.pyplot as pyplot

def show_image (path:str)->None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Agu", "Sep", "Oct", "Nov", "Dec"]

temperatures = [14.3, 13.3, 15.0, 14.7, 14.7,
                14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]

pyplot.plot(months, temperatures)

pyplot.savefig('./assets/out/temperatureBogota.png')

show_image('./assets/out/temperatureBogota.png')


