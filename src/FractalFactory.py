from Fractal import Julia, Mbrot, BurningShipJulia


def makeFractal(fractalInfo):
    if fractalInfo['type'] == 'julia':
        return Julia(fractalInfo)
    elif fractalInfo['type'] == 'mandelbrot':
        return Mbrot(fractalInfo)
    elif fractalInfo['type'] == 'burningshipjulia':
        return BurningShipJulia(fractalInfo)
    else:
        raise NotImplementedError("Unrecognized fractal type")
