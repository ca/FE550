import matplotlib.pyplot as plt
import numpy as np
import csv


with open('percent-bachelors-degrees-women-usa.csv', 'rU') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print row

def lineplot(x_data, y_data, x_label="", y_label="", title=""):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

# lineplot([], [], "", "", "Percentage of Bachelor's degrees conferred to women in the U.S.A., by major (1970-2012)")