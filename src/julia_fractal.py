# Julia Set Visualizer

import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop

shapes = {
        'fulljulia': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  4.0, },

        'hourglass': {
            'centerX':     0.618,
            'centerY':     0.00,
            'axisLength':  0.017148277367054, },

        'lace-curtains': {
            'centerX': -1.01537721564149,
            'centerY': 0.249425427273733,
            'axisLength': 0.0121221433855615, },

        'lakes': {
            'centerX': -0.339230468501458,
            'centerY': 0.417970758224314,
            'axisLength': 0.164938488846612, }
        }

palette = [
        '#ffe4b5', '#ffe5b2', '#ffe7ae', '#ffe9ab', '#ffeaa8', '#ffeda4',
        '#ffefa1', '#fff29e', '#fff49a', '#fff797', '#fffb94', '#fffe90',
        '#fcff8d', '#f8ff8a', '#f4ff86', '#f0ff83', '#ebff80', '#e7ff7c',
        '#e2ff79', '#ddff76', '#d7ff72', '#d2ff6f', '#ccff6c', '#c6ff68',
        '#bfff65', '#b9ff62', '#b2ff5e', '#abff5b', '#a4ff58', '#9dff54',
        '#95ff51', '#8dff4e', '#85ff4a', '#7dff47', '#75ff44', '#6cff40',
        '#63ff3d', '#5aff3a', '#51ff36', '#47ff33', '#3eff30', '#34ff2c',
        '#2aff29', '#26ff2c', '#22ff30', '#1fff34', '#1cff38', '#18ff3d',
        '#15ff42', '#11ff47', '#0eff4c', '#0bff51', '#07ff57', '#04ff5d',
        '#01ff63', '#00fc69', '#00f970', '#00f677', '#00f27d', '#00ef83',
        '#00ec89', '#00e88e', '#00e594', '#00e299', '#00de9e', '#00dba3',
        '#00d8a7', '#00d4ab', '#00d1af', '#00ceb3', '#00cab7', '#00c7ba',
        '#00c4be', '#00c0c0', '#00b7bd', '#00adba', '#00a4b6', '#009cb3',
        '#0093b0', '#008bac', '#0082a9', '#007ba6', '#0073a2', '#006b9f',
        '#00649c', '#005d98', '#005695', '#004f92', '#00498e', '#00438b',
        '#003d88', '#003784', '#003181', '#002c7e', '#00277a', '#002277']

GREY0 = '#000000'


def getPixelColor(z, colors):
    """Return corresponding color from palette depending on iterations to get to two
    If nothing above two is found, return last color in palette"""

    c = complex(-1, 0)  # initial c0

    for color in colors:
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2:  # two is target number
            return color

    # if no iteration reaches TWO, return last color in palette
    return colors[78]


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
    """The main entry-point for the Julia fractal generator"""

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
