import numpy
import matplotlib

matplotlib.use("AGG")
from matplotlib import pyplot


def plot_stroke(stroke, save_name=None):
    # Plot a single example.
    f, ax = pyplot.subplots()

    x = numpy.cumsum(stroke[:, 1])
    y = numpy.cumsum(stroke[:, 2])

    size_x = x.max() - x.min() 
    size_y = y.max() - y.min() 

    f.set_size_inches(5.0 * (size_x / size_y * 0.9), 5.0)

    cuts = numpy.where(stroke[:, 0] == 1)[0]
    start = 0

    for cut_value in cuts:
        ax.plot(x[start:cut_value], y[start:cut_value], "k-", linewidth=3)
        start = cut_value + 1

    ax.axis("off")  # equal
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    if save_name is None:
        pyplot.show()
    else:
        try:
            pyplot.tight_layout()
            pyplot.savefig(save_name, format='svg',pad_inches=0)
        except Exception:
            print("Error building image!: " + save_name)

    pyplot.close()

# import numpy as np
# import matplotlib.pyplot as plt

# def plot_strokes(strokes, save_name=None):
#     print("cock")
#     # Plot multiple strokes
#     fig, ax = plt.subplots()

#     max_x, max_y = float('-inf'), float('-inf')
#     min_x, min_y = float('inf'), float('inf')

#     for stroke in strokes:
#         x = np.cumsum(stroke[:, 1])
#         y = np.cumsum(stroke[:, 2])

#         max_x = max(max_x, x.max())
#         max_y = max(max_y, y.max())
#         min_x = min(min_x, x.min())
#         min_y = min(min_y, y.min())

#         cuts = np.where(stroke[:, 0] == 1)[0]
#         start = 0

#         for cut_value in cuts:
#             ax.plot(x[start:cut_value], y[start:cut_value], "k-", linewidth=3)
#             start = cut_value + 1
        
#         # Plot the last segment if it doesn't end with a cut
#         if start < len(x):
#             ax.plot(x[start:], y[start:], "k-", linewidth=3)

#     size_x = max_x - min_x + 1.0
#     size_y = max_y - min_y + 1.0

#     fig.set_size_inches(5.0 * (size_x / size_y * 0.9), 5.0)

#     ax.axis("off")
#     ax.axes.get_xaxis().set_visible(False)
#     ax.axes.get_yaxis().set_visible(False)

#     if save_name is None:
#         plt.show()
#     else:
#         try:
#             plt.savefig(save_name + ".svg", bbox_inches="tight", pad_inches=0.5)
#         except Exception as e:
#             print(f"Error building image!: {save_name}")
#             print(f"Exception: {e}")

#     plt.close()
    
