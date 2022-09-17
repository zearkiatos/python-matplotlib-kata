import random
import matplotlib.pyplot as pyplot

notes = []
students_ids = []


def show_image(path: str) -> None:
    image = pyplot.imread(path).tolist()
    pyplot.imshow(image)
    pyplot.show()


for i in range(30):
    generated_note = random.normalvariate(3.25, 0.98)
    generated_note = round(generated_note, 2)
    added = False
    while not added:
        generated_id = random.randint(20202001, 20202999)
        generated_id = str(generated_id)
        if generated_id not in students_ids:
            notes.append(generated_note)
            students_ids.append(generated_id)
            added = True


pyplot.plot(students_ids, notes)
pyplot.title('Course Notes')
pyplot.ylabel('Note')
pyplot.xlabel('Student ID')
pyplot.xticks(rotation=90)

pyplot.savefig('./assets/out/notes.png')

show_image('./assets/out/notes.png')

pyplot.hist(notes, bins=4, color=["green"], edgecolor="black", linewidth=1)
pyplot.title("Students quantity by note range")
pyplot.ylabel("Note range")

pyplot.savefig('./assets/out/histogramNotes.png')

show_image('./assets/out/histogramNotes.png')

pyplot.scatter(students_ids, notes)
pyplot.title("Course notes")
pyplot.ylabel("Note")
pyplot.xlabel("Student ID")
pyplot.xticks(rotation=90)

pyplot.savefig('./assets/out/scatterNotes.png')

show_image('./assets/out/scatterNotes.png')

