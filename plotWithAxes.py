import matplotlib.pyplot as pyplot

def show_image (path:str)->None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Agu", "Sep", "Oct", "Nov", "Dec"]

temperatures = [14.3, 13.3, 15.0, 14.7, 14.7,
                14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]

figure = pyplot.figure(figsize=(7,4))

axel = figure.add_axes([0.1,0.1,0.8,0.8])

axel.plot(months, temperatures, label = "Temperature")
axel.set_xlabel("Months")

axel.set_ylabel("Temperature")

axel.set_title("Average temperature in Bogotá per month (1970 - 2000)")

axel.legend()

figure.savefig('./assets/out/temperatureBogotaAxel.png')

show_image('./assets/out/temperatureBogotaAxel.png')


