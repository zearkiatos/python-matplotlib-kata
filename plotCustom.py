import matplotlib.pyplot as pyplot

def show_image (path:str)->None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Agu", "Sep", "Oct", "Nov", "Dec"]

temperatures = [14.3, 13.3, 15.0, 14.7, 14.7,
                14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]

pyplot.plot(figsize = (7,4))
pyplot.plot(months, temperatures, label = "Temperature")

pyplot.xlabel("Month")
pyplot.ylabel("Temperature")
pyplot.title("Average temperature in Bogotá per month (1970 - 2000)")
pyplot.legend()


pyplot.savefig('./assets/out/temperatureBogotaDetails.png')

show_image('./assets/out/temperatureBogotaDetails.png')