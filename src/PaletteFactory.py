from Palette import Mismatch, Complementary


def makePalette(maxIter, palette):
    if palette == "mismatch":
        return Mismatch(maxIter)
    elif palette == "complementary":
        return Complementary(maxIter)
    else:
        raise NotImplementedError("Invalid palette requested")
