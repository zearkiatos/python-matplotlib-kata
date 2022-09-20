import matplotlib.pyplot as pyplot


def show_image(path: str) -> None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


background_color = "#009ACC"
temperature_color = "#005587"
precipitation_color = "#880000"

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Agu", "Sep", "Oct", "Nov", "Dec"]
precipitations = [40, 60, 115, 120, 125, 55, 50, 55, 110, 120, 130, 60]

temperatures = [14.3, 13.3, 15.0, 14.7, 14.7,
                14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]

figure = pyplot.figure(figsize=(7, 4))


axel = figure.add_axes([0.1, 0.1, 0.8, 0.8])
axel.set_alpha(0.9)
axel.set_facecolor(background_color)
axel.grid(True)
axel.plot(months, temperatures, color=temperature_color,
          linewidth=1.5, linestyle='-',  marker='o', markersize=6, markerfacecolor="blue", label="Temperature")
axel.set_xlabel("Months", style="italic", fontweight="bold")

axel.set_ylabel("Temperature", fontweight="bold")
for label in axel.get_yticklabels():
    label.set_color(temperature_color)
axel.set_ylim(10, 20)

axel.set_title(
    "Average temperature in Bogotá per month (1970 - 2000)", fontweight="bold")

axelPrecipitation = axel.twinx()
axelPrecipitation.plot(
    months, precipitations, color=precipitation_color, linewidth=1.5, ls='-', marker='s', markersize=8, markerfacecolor="red", label="Temperature")
axelPrecipitation.set_ylabel(
    "Precipitation", color=precipitation_color, fontweight="bold")
for label in axelPrecipitation.get_yticklabels():
    label.set_color(precipitation_color)
axelPrecipitation.set_ylim(0, 200)
axel.legend()

figure.savefig('./assets/out/axelReference.png')

show_image('./assets/out/axelReference.png')
