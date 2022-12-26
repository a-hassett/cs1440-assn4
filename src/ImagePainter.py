from tkinter import Tk, Canvas, PhotoImage, mainloop
import time


class ImagePainter:
    def __init__(self, fractal, palette, outfile):
        before = time.time()

        imageSize = fractal.getImageSize()
        window = Tk()
        img = PhotoImage(width=imageSize, height=imageSize)

        canvas = Canvas(window, width=imageSize, height=imageSize, bg='#000000')
        canvas.pack()
        canvas.create_image((imageSize / 2, imageSize / 2), image=img, state="normal")

        for row in range(imageSize, 0, -1):
            for col in range(imageSize):
                x = fractal.getMinX() + col * fractal.getPixelSize()
                y = fractal.getMinY() + row * fractal.getPixelSize()
                color = palette.getColor(fractal.count(complex(x, y)))
                img.put(color, (col, imageSize - row))
            window.update()

        img.write(outfile)
        print(f"Wrote picture {outfile}")

        after = time.time()
        print(f"Done in {after - before:.3f} seconds!")

        mainloop()
