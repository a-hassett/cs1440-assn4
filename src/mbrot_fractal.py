# Mandelbrot Set Visualizer  	         	  

import sys  	         	  
import time  	         	  
from tkinter import Tk, Canvas, PhotoImage, mainloop  	         	  

shapes = {
        'elephants': {
            'centerX':  0.30820836067024604,
            'centerY':  0.030620936230004017,
            'axisLength':  0.03, },

        'leaf': {
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLength':  0.000051248888, },

        'mandelbrot': {
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLength': 2.5, },

        'mandelbrot-zoomed': {
            'centerX': -1.0,
            'centerY': 0.0,
            'axisLength': 1.0, },

        'seahorse': {
            'centerX': -0.745,
            'centerY': 0.105,
            'axisLength': 0.01, },

        'spiral0': {
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLength': 0.004978179931102462, },

        'spiral1': {
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLength': 0.002, },

        'starfish': {
            'centerX': -0.463595023481762,
            'centerY': 0.598380871135558,
            'axisLength': 0.00128413675654471, }
        }

palette = [
    '#89ff00', '#a4f817', '#baf12e', '#ccec43', '#d9e758', '#e3e46b', '#e1d97e',
    '#e0d18f', '#dfce9f', '#e0ceaf', '#e1d1bd', '#e4d6cb', '#e7ddd7', '#ece5e3',
    '#f1eeed', '#f8f7f7', '#ffffff', '#f8f7f7', '#f1eeed', '#ece4e3', '#e7dbd7',
    '#e4d3cb', '#e1cbbd', '#e0c4af', '#dfbf9f', '#e0bd8f', '#e1bc7e', '#e4bf6b',
    '#e7c458', '#eccd43', '#f1da2e', '#f8eb17', '#fdff00', '#f8eb17', '#f1da2e',
    '#eccd43', '#e7c458', '#e4bf6b', '#e1bc7e', '#e0bd8f', '#dfbf9f', '#e0c4af',
    '#e1cbbd', '#e4d3cb', '#e7dbd7', '#ece4e3', '#f1eeed', '#f8f7f7', '#ffffff',
    '#f7f6f6', '#f1eded', '#ebe4e2', '#e6dad7', '#e3d0ca', '#e0c6bd', '#debeae',
    '#deb69f', '#deaf8e', '#dfaa7d', '#e1a66b', '#e4a557', '#e9a643', '#eea92e',
    '#f4af17', '#f7b604', '#f4af17', '#eea92e', '#e9a643', '#e4a557', '#e1a66b',
    '#dfaa7d', '#deaf8e', '#deb69f', '#debeae', '#e0c6bd', '#e3d0ca', '#e6dad7',
    '#ebe4e2', '#f1eded', '#f7f6f6', '#ffffff', '#f8f7f7', '#f2f1ef', '#ebece5',
    '#e2e7db', '#d3e3d0', '#c5e0ca', '#b9ddce', '#abdbd9', '#9ec8da', '#8fa7da',
    '#8480db', '#9c70dc', '#c25fde', '#e04dcb', '#e43b8d', '#ffffff', '#f7f6f6',
    '#f0efec', '#e8eae1', '#dae5d5', '#c8e1cb', '#badecd', '#abdbd9', '#9cc4da',
    '#8b9cda', '#8d79db', '#b066dd', '#e052da', '#e33e97', '#e8283f']

GREY0 = '#000000'


def getPixelColor(c, colors):
    """Return corresponding color from palette depending on iterations to get to two
    If nothing above two is found, return last color in palette"""

    z = complex(0, 0)  # initial z0

    for color in colors:
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2:  # two is target number
            z = float(2)
            return color

    return colors[-1]


def makeFractal(fractal, window, photoImage, bg_color, imageSize):
    """Paint a Fractal image into the TKinter PhotoImage canvas."""

    minx = fractal['centerX'] - (fractal['axisLength'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLength'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLength'] / 2.0)

    pixelSize = abs(maxx - minx) / imageSize

    # Display the image on the screen
    canvas = Canvas(window, width=imageSize, height=imageSize, bg=bg_color)
    canvas.pack()
    canvas.create_image((imageSize / 2, imageSize / 2), image=photoImage, state="normal")

    for row in range(imageSize, 0, -1):
        for col in range(imageSize):
            x = minx + col * pixelSize
            y = miny + row * pixelSize
            color = getPixelColor(complex(x, y), palette)
            photoImage.put(color, (col, imageSize - row))
        window.update()  # display a row of pixels at a time


def main(imageArg):
    """The main entry-point for the MBot fractal generator"""

    before = time.time()
    window = Tk()
    img = PhotoImage(width=512, height=512)
    makeFractal(shapes[imageArg], window, img, GREY0, 512)

    # save the image as a PNG file
    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(imageArg + ".png")
    print("Wrote picture " + imageArg + ".png")

    # Call tkinter.mainloop so the GUI remains open
    print("Close the image window to exit the program")
    mainloop()