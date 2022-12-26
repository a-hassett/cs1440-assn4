class Fractal:
    def __init__(self, fractalInfo):
        self.__FractalInfo = fractalInfo

    def count(self, complexNum):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

    def getImageSize(self):
        return self.__FractalInfo['pixels']

    def getMinX(self):
        return self.__FractalInfo['centerx'] - (self.__FractalInfo['axislength'] / 2.0)

    def getMinY(self):
        return self.__FractalInfo['centery'] - (self.__FractalInfo['axislength'] / 2.0)

    def getPixelSize(self):
        maxx = self.__FractalInfo['centerx'] + (self.__FractalInfo['axislength'] / 2.0)
        return abs(maxx - self.getMinX()) / self.getImageSize()


class Julia(Fractal):
    def __init__(self, fractalInfo):
        super().__init__(fractalInfo)
        self.__FractalInfo = fractalInfo

    def count(self, z):
        c = complex(self.__FractalInfo['creal'], self.__FractalInfo['cimag'])

        for palette_index in range(self.__FractalInfo['iterations']):
            z = z * z + c
            if abs(z) > 2:
                return palette_index

        return self.__FractalInfo['iterations'] - 1

    def getImageSize(self):
        return super().getImageSize()

    def getMinX(self):
        return super().getMinX()

    def getMinY(self):
        return super().getMinY()

    def getPixelSize(self):
        return super().getPixelSize()


class Mbrot(Fractal):
    def __init__(self, fractalInfo):
        super().__init__(fractalInfo)
        self.__FractalInfo = fractalInfo

    def count(self, c):
        z = complex(0, 0)

        for palette_index in range(self.__FractalInfo['iterations']):
            z = z * z + c
            if abs(z) > 2:
                return palette_index

        return self.__FractalInfo['iterations'] - 1

    def getImageSize(self):
        return super().getImageSize()

    def getMinX(self):
        return super().getMinX()

    def getMinY(self):
        return super().getMinY()

    def getPixelSize(self):
        return super().getPixelSize()


class BurningShipJulia(Fractal):
    def __init__(self, fractalInfo):
        super().__init__(fractalInfo)
        self.__FractalInfo = fractalInfo

    def count(self, z):
        c = complex(self.__FractalInfo['creal'], self.__FractalInfo['cimag'])

        for palette_index in range(self.__FractalInfo['iterations']):
            zabs = complex(abs(z.real), abs(z.imag))
            z = zabs * zabs - c
            if abs(z) > 2:
                return palette_index

        return self.__FractalInfo['iterations'] - 1

    def getImageSize(self):
        return super().getImageSize()

    def getMinX(self):
        return super().getMinX()

    def getMinY(self):
        return super().getMinY()

    def getPixelSize(self):
        return super().getPixelSize()