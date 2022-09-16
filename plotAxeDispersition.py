import matplotlib.pyplot as pyplot
import random

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Agu", "Sep", "Oct", "Nov", "Dec"]


def show_image(path: str) -> None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


def get_random_temperatures_by_cities(cities: list) -> dict:
    temperatures = {}
    for city in cities:
        temperatures[city] = []

    for city in cities:
        count = 0
        while(count < len(months)):
            temperatures[city].append(random.randrange(-10, 30))
            count += 1

    return temperatures


def get_random_precipitations_by_cities(cities: list) -> dict:
    precipitations = {}
    for city in cities:
        precipitations[city] = []

    for city in cities:
        count = 0
        while(count < len(months)):
            precipitations[city].append(random.randrange(0, 500))
            count += 1

    return precipitations


figure, axes = pyplot.subplots(2, 3, figsize=(12, 8), sharex=True, sharey=True)

cities = [
    "Bogotá",
    "Baranquilla",
    "Cali",
    "Medellin",
    "Florencia",
    "Valledupar"
]

temperatures = get_random_temperatures_by_cities(cities)
precipitations = get_random_precipitations_by_cities(cities)


city_number = 0
city_list = list(cities)
for row in axes:
    for axe in row:
        axe.plot(
            months, temperatures[city_list[city_number]], "r", label="Temperature")
        axe.set_xticklabels(months)
        axe.set_xlabel("Month")
        axe.set_ylabel("Temperature")
        axe.set_title(city_list[city_number])
        city_number += 1
pyplot.tight_layout()

axe = figure.add_axes([0.5, 0.3, 0.4, 0.4])

for city in city_list:
    axe.scatter(temperatures[city], precipitations[city], label=city)
axe.set_title("Temperature vs. \n Precipitation", loc="left")


figure.savefig('./assets/out/temperatureVsPresipitations.png')

show_image('./assets/out/temperatureVsPresipitations.png')
