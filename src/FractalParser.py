class FractalParser:
    def __init__(self, filename):
        self.__infoTypes = {'type': str,
                            'pixels': int,
                            'centerx': float,
                            'centery': float,
                            'axislength': float,
                            'iterations': int,
                            'creal': float,
                            'cimag': float, }
        self.__filename = filename

    def outfile(self):
        if self.__filename == "default":
            return "default.png"

        first = self.__filename.rfind("/")
        last = self.__filename.rfind(".")
        return self.__filename[first + 1: last] + ".png"

    def buildDictionary(self):
        if self.__filename == "default":
            # default FractalInfo dictionary will be seahorse
            print("Creating default fractal")
            return {'type': 'mandelbrot',
                    'pixels': 640,
                    'centerx': -0.745,
                    'centery': 0.105,
                    'axislength': 0.01,
                    'iterations': 256, }
        else:
            file = open(self.__filename)
            tempDict = {}

        while True:
            line = file.readline()
            self.updateDictionary(line, tempDict)

            if not line:
                break

        if (tempDict['type'] == 'julia' or tempDict['type'] == 'burningshipjulia') and ('creal' and 'cimag' not in tempDict):
            raise NotImplementedError("Julia-type fractals must contain data for cReal and cImag")

        for key, value in self.__infoTypes.items():
            if key not in tempDict and (key != 'creal' and key != 'cimag'):
                raise NotImplementedError(f"The data for {key} is not found in the file")

        file.close()
        return tempDict

    def updateDictionary(self, line, tempDict):
        if ":" in line:
            line.lower()

            # reformat the line into a list with the data type key and the corresponding data
            line = line.replace(" ", "").lower().strip().split(":")

            key = line[0]
            data = line[1]

            # if the key is valid and its corresponding data is valid, add it to the dictionary
            if key in self.__infoTypes and self.__isCorrectType(key, data, self.__infoTypes[key]):
                tempDict.update({key: self.__infoTypes[key](data)})  # add line information to dictionary

    def __isCorrectType(self, key, data, ofType):
        try:
            ofType(data)
            return True
        except ValueError:
            raise RuntimeError(f"File's {key} did not contain {ofType} information")
            # return False
