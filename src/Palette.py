from colour import Color

lightPink = "#FF9797"
darkPink = "#F65353"
darkOrange = "#FF7F1A"
lightOrange = "#F59A23"
yellow = "#FFE785"
lightGreen = "#7EC636"
darkGreen = "#007355"
darkBlue = "#03468F"
lightBlue = "#0000D5"
purple = "#82218B"
black = "#000000"
grey = "#9B9B9B"


class Palette:
    def __init__(self, maxIter):
        self.__maxIter = maxIter

    def getColor(self, count):
        raise NotImplementedError("Concrete subclass of Palette method must implement getColor() method")


class Mismatch(Palette):
    def __init__(self, maxIter):
        super().__init__(maxIter)
        self.__maxIter = maxIter

        colors = [darkGreen, black, lightOrange, black, yellow, black, purple, black, lightPink, black, lightGreen,
                  black, lightGreen, black, lightBlue, black, darkPink, black]  # list of colors i want in my palette
        self.palette = []  # list of RGB gradient between colors list

        for i in range(len(colors) - 1):
            start = Color(colors[i])
            end = colors[i + 1]

            fill = self.__maxIter % (len(colors) - 1)
            if i < fill:
                extra = 2
            else:
                extra = 1

            for c in start.range_to(end, self.__maxIter // (len(colors) - 1) + extra):
                self.palette.append(c.hex_l)
            self.palette.pop()

    def getColor(self, count):
        return self.palette[count]


class Complementary(Palette):
    def __init__(self, maxIter):
        super().__init__(maxIter)
        self.__maxIter = maxIter
        self.palette = []  # list of RGB gradient between colors list

        colors = [lightOrange, black, lightBlue, black, yellow, black, darkOrange, black, darkBlue, black,
                  grey, black]  # list of colors i want in my palette

        for i in range(len(colors) - 1):
            start = Color(colors[i])
            end = colors[i + 1]

            fill = self.__maxIter % (len(colors) - 1)
            if i < fill:
                extra = 2
            else:
                extra = 1

            for c in start.range_to(end, self.__maxIter // (len(colors) - 1) + extra):
                self.palette.append(c.hex_l)
            self.palette.pop()

    def getColor(self, count):
        return self.palette[count]
