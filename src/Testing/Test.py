import unittest
import FractalParser


class Test(unittest.TestCase):
    def test_dictionaryCompilation(self):
        file = '''# The characteristic Mandelbrot shape embedded within an 8-pointed compass
                type: Mandelbrot
                pixels: 1024
                centerX: -1.999774061505
                centerY: -0.0
                axisLength: 0.000000361314
                iterations: 350'''
        print(file)
        fp = FractalParser(file)
        # self.assertEqual(pixelsWrittenSoFar(640, 480), 307200)


if __name__ == '__main__':
    unittest.main()
