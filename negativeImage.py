import numpy as numpy
import matplotlib.pyplot as pyplot
import matplotlib.image as matplotimage


def load_image(path: str) -> list:
    image = matplotimage.imread(path).tolist()
    return image


def negative_filter(image: list)->list:
    for row in range(len(image)):
        for column in range(len(image[row])):
            pixels = image[row][column]

            for k in range(3):
                image[row][column][k] = abs(pixels[k] - 1)

    return image


def show_image(image: list) -> list:
    pyplot.imshow(image)
    pyplot.show()


image = load_image('./assets/Landscape-BW.jpeg')

show_image(image)

negative_image = negative_filter(image)

show_image(negative_image)
