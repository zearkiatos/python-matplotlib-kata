import matplotlib.pyplot as pyplot
import matplotlib.image as image

img = image.imread('./assets/starwars.jpeg')

img_plot = pyplot.imshow(img)

print(img_plot)