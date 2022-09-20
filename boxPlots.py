import matplotlib.pyplot as pyplot

def show_image (path:str)->None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()

figure = pyplot.figure(figsize=(9, 6))

axe = figure.add_axes([0.1, 0.1, 0.8, 0.8])

precipitations = [40, 60, 115, 120, 125, 55, 50, 55, 110, 120, 130, 60]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Agu", "Sep", "Oct", "Nov", "Dec"]

meanpointprops = {
    "marker": "D",
    "markeredgecolor": "black",
    "markerfacecolor": "firebrick"
}

axe.boxplot(precipitations, labels=months, showmeans=True,
            meanline=True, meanprops=meanpointprops)
axe.set_title("Variation")

axe.set_ylabel('Precipitation')

pyplot.savefig('./assets/out/boxPlots.png')

show_image('./assets/out/boxPlots.png')