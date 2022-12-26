import unittest
from FractalParser import FractalParser
import FractalFactory
from Fractal import Fractal, Julia, Mbrot, BurningShipJulia
import PaletteFactory
from Palette import Palette, Complementary, Mismatch


class Test(unittest.TestCase):
    def test_dictionaryCompilation(self):
        file = "hello.frac"
        dict = {}
        fp = FractalParser(file)
        fp.updateDictionary("TypE : ManDelbrOt\n", dict)
        self.assertTrue(dict == {'type': 'mandelbrot'})

    def test_outfile(self):
        fp1 = FractalParser("default")
        self.assertEqual(fp1.outfile(), "default.png")
        fp2 = FractalParser("src/fun.frac")
        self.assertEqual(fp2.outfile(), "fun.png")

    def test_fractalFactoryTypes(self):
        info = {'type': 'mandelbrot'}
        self.assertEqual(type(FractalFactory.makeFractal(info)), Mbrot)

    def test_paletteFactoryTypes(self):
        info = 'complementary'
        self.assertEqual(type(PaletteFactory.makePalette(25, info)), Complementary)

    def test_paletteLength(self):
        max = 25
        palette = Complementary(max)
        self.assertEqual(len(palette.palette), 25)

    def test_abstractFractalError(self):
        dict = {}
        fractal = Fractal(dict)
        try:
            fractal.count(4)
            self.assertEquals(1, 2)
        except NotImplementedError:
            self.assertEquals(1, 1)

    def test_abstractPaletteError(self):
        palette = Palette(12)
        try:
            palette.getColor(4)
            self.assertEquals(1, 2)
        except NotImplementedError:
            self.assertEquals(1, 1)


if __name__ == '__main__':
    unittest.main()
