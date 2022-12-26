import sys
from FractalParser import FractalParser
import FractalFactory
import PaletteFactory
from ImagePainter import ImagePainter

if len(sys.argv) == 1:
    filename = "default"
    palettename = "complementary"
    print("Creating default color palette")

elif len(sys.argv) == 2:
    filename = sys.argv[1]
    palettename = "complementary"
    print("Creating default color palette")
else:
    filename = sys.argv[1]
    palettename = sys.argv[2].lower()

fp = FractalParser(filename)
FractalInfo = fp.buildDictionary()
fractal = FractalFactory.makeFractal(FractalInfo)
palette = PaletteFactory.makePalette(FractalInfo['iterations'], palettename)

ImagePainter(fractal, palette, fp.outfile())
