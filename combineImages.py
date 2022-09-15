import numpy as numpy
import matplotlib.pyplot as pyplot
import matplotlib.image as matplotimage


def combine_images(red, green, blue):
    red_image = matplotimage.imread(red)
    green_image = matplotimage.imread(green)
    blue_image = matplotimage.imread(blue)

    red_component = red_image[:, :, 0]
    green_component = green_image[:, :, 1]
    blue_component = blue_image[:, :, 2]

    rgb = numpy.dstack((red_component, green_component, blue_component))

    return rgb

img_red = './assets/Landscape-BW.jpeg'
img_green = './assets/Landscape-BW.jpeg'
img_blue = './assets/Landscape-BW.jpeg'


image = combine_images(img_red, img_green, img_blue)

img_plot = pyplot.imshow(image)