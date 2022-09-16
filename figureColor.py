import matplotlib.pyplot as pyplot


def show_image(path: str) -> None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


background_color = "#444444"
temperature_color = "#FFAF5E"
presipitation_color = "#3399dc"


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Agu", "Sep", "Oct", "Nov", "Dec"]

temperatures = [14.3, 13.3, 15.0, 14.7, 14.7,
                14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]

precipitations = [40, 60, 115, 120, 125, 55, 50, 55, 110, 120, 130, 60]

figure = pyplot.figure(figsize=(7, 4))

axel = figure.add_axes([0.1, 0.1, 0.8, 0.8])
axel.set_facecolor(background_color)
axel.set_alpha(0.9)

axel.plot(months, temperatures, color=temperature_color,
          linewidth=2.15, linestyle='--', marker='s', markersize=6, markerfacecolor="red", label="Temperature")
axel.set_xlabel("Months")

axel.set_ylabel("Temperature", color=temperature_color)

axel.set_title("Average temperature in Bogotá per month (1970 - 2000)")

axelPrecipitation = axel.twinx()

axelPrecipitation.plot(months, precipitations,
                       color=presipitation_color, linewidth=1.55, ls='-.', marker='o', markersize=8, markerfacecolor="blue", markeredgewidth=3, markeredgecolor="yellow",  label="precipitation")

axelPrecipitation.set_ylabel("Precipitation", color=presipitation_color)

axel.legend()

figure.savefig('./assets/out/temperatureCustomColor.png')

show_image('./assets/out/temperatureCustomColor.png')
