import sys
sys.path.insert(0, r"../") # Ajout du dossier dans le path python pour import

import pytest
import numpy as np
import matplotlib.pyplot as plt; from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

import archi.im_proc as aim

@pytest.fixture(autouse=False)
def show(request):
    request.addfinalizer(plt.show)

@pytest.fixture()
def image_gray():
    return np.array([[0, 1, 0], [1, 1, 1], [1, 1, 0]])

@pytest.fixture()
def image_color():
    return np.array([[[0, 1, 0], [0, 1, 0], [0, 1, 0]],
                     [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                     [[1, 1, 0], [1, 1, 0], [1, 1, 0]]])*255


def test_display_image(image_color, image_gray):
    # A revoir : essayer de de récupérer l'image originale à partir de la figu-
    # re matplotlib.
    displayer = aim.Displayer()
    figure = displayer.display_image(image_color)
    
    # figure.canvas.draw()
    # width, height = figure.get_size_inches() * figure.get_dpi() 
    # width, height = int(width), int(height)
    # image = np.fromstring(figure.canvas.tostring_rgb(), dtype=np.uint8).reshape((height,width,3))

    # displayer.display_image(image_gray)

def test_display_histogram(image_gray, image_color):
    displayer = aim.Displayer()
    displayer.display_histogram(image_gray)
    displayer.display_histogram(image_color, rgb=True)

    
    


