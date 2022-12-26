# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

This sprint of Assignment 4 will continue with the fractals we have been working
with. We're going to be adding a few features though and I will have to further
refactor the modules so that they're more fit to accomodate the new features. We will
have to change the program so that the command line can accept up to two arguments
after the program name "src/main.py". These two arguments are both optional, because 
we will set up a default option for both. The first argument will be the name of the 
.frac file that will contain all the specifications for the fractal (like the name, 
type, size in pixels, centerX, centerY, iterations, and axisLength). Some .frac files will also 
include creal and cimag which are the real and imaginary components of c, the Julia
constant. The creal and cimag options will only be used for Julia and Burningshipjulia
type fractals. The name of the fractal is an optional argument as well.
The module FractalParser will read the .frac files and pull out the required information
from each. It will give put all the information into a dictionary FractalInfo which is then
provided to FractalFactory when the fractal objects are being made. FractalParser will
be where the given file name is checked for its existence. If it doesn't exist, we will
let the program fail. If the file exists, we will read it. If the type of fractal in there
is not julia, mandelbrot, or one of the extra types we will make (I'll choose between 
Mandelbrot3, Mandelbrot4, Phoenix, Burningshipjulia, and Burningship), we will raise a
NotImplementedError. If the file exists but has any other errors, we will raise a
RuntimeError. When FractalParser reads the file, it will give the iteration count, which
should be an integer, directly to Palette so it can build a dynamic color palette
based on the iterations. We will give the rest of the information in dictionary form to
FractalFactory. The second optional argument on the command line is the color
scheme of the image. We will be making two aesthetically-pleasing but still dynamic color
palettes. This argument is where we pick which one to use.\
\
Now that we've established what happens with the command line, let's look a little deeper
into the inner-workings of Assn3. After we get all the necessary information from the .frac
file using the handy dandy FractalParser, we will throw the resulting dictionary into a
Fractal object. The Fractal class will be abstract with three concrete subclasses, each of
a different type (I specified the types in the above paragraph). The Fractal subclasses
will each contain the different formulas that are required to make the fractals (the ones
that use z and c). The formula will be found in the count() method which returns the number
of iterations that each pixel should perform. We previously called count() getPixelColor().
Now it will have the parameters self and a complex number. It will return the number of
iterations needed.\
\
FractalFactory will build a fractal type based on the type given in the dictionary input. 
If no fractal type is given because there was no command line argument given, FractalFactory
will choose the default. It will accept the FractalInfo dictionary as input. If this dictionary
"type" is empty, that is when we will choose the default. I might change this to be done in 
FractalParser instead. I think it would easier to see that there is no file and then give
the default dictionary to FractalFactory. Either way, you will build the fractal class with
its respective type in this class by using fractal = *fractaltype*(fractalInfo) where the
fractal type utilizes polymorphism and we no longer have to acknowledge any difference
between the types after its initialization and the fractalInfo is the name of the
dictionary. The only difference between the types is the count() method found in the 
Fractal abstract class and its concrete subclasses. Besides that, and maybe a few other
methods, all of the types will be treated the same.\
\
FractalParser provides the iteration max count from the .frac file to PaletteFactory which
is where the Palette class is built. It's also where the default Palette is defined. We will 
also check whether the second command line argument (after src/main.py) is a valid Palette
name. If it's not this is where we will raise a NotImplementedError("Invalid palette requested").
The Palette it builds will use an abstract class to create a skeleton for the palette
which will extend into two different concrete subclasses. I will have to make them pretty.
I'll think I'll make one that's like a rainbow with black separating the colors. And I think
I'll make one with reds, oranges, and blues (and black and white). I think that would look cool.\
\
ImagePainter is the module where the fractal will be painted. It will take input from
PaletteFactory where the Palette is built and FractalFactory where the Fractal is built.
It will use these objects. I'll iterate through every pixel in the image and use Fractal's
count() method to see which color that pixel should be. I'll figure out how many pixels
to use by using the fractalInfo dictionary. The pixel count should be in there and we'll
get it from FractalFactory. I'll also get the minx, miny, and maxx from that dictionary.
I want to calculate these, the pixel size in FractalParser so I don't have to muddy-up the code
in ImagePainter. The main.py module will create the ImagePainter object.


## Phase 1: System Analysis *(10%)*

__Main.py :__ The main driver will take command line arguments from the user. We will give 
FractalParser the string for sys.argv[1] if it exists. If it does not, we will give the string
"default frac". We will either give FractalParser the sys.argv[2] string or "default palette".
This module will also create the ImagePainter object.\
\
__FractalParser.py :__ This object will be created by main.py with the string parameters
fracfile and palette. If fracfile is the string "default frac", we'll create a default dictionary
to use later. If it's anything else, we'll attempt to open the file. If it doesn't exist, we'll
allow the program to fail. Once we open the file, we'll read from it line by line. In each line,
we'll look for a colon. We'll check the word before the colon for one of the desired parameters
(type, pixels, centerX, centerY, axisLength, and iterations) and the optional parameters (cReal
and cImag) if the type is julia or burningshipjulia. We need to make sure to make everything lowercase.
After we identify the dictionary key part of the file, we need to check that the matching data is of 
the right type. The "type" must be a string that is "julia", "mandelbrot", or "extra". The "pixels" 
must be an integer between 256 and 640. The "centerX" must be a float within the range of the image
size. The "centerY" must be a float within the image size. The "axisLength" must be a float. The "iterations"
must be an integer between 64 and 256. The "cReal" and "cImag" must be floats. I'll have to override
I can organize the lines using "line.replace(" ", "").strip().split(":")" which will produce
a list of just the words in the line. But first I'll want to check if there's a colon in the line at
all because if there's not I won't need to use it at all. We need to check that the data is of the
correct type as specified above. We can make a function to check if the type is correct using
parameters of the string to check and the type to check. Once all the data is in lists after being
split and stripped, I will have to turn them into dictionaries. I can do this by appending all
the line-lists into a larger list. Then I can use a for loop for every item in that list
to add to a dictionary using for i in allitems: dictionary.update({i[0]: i[1]}). We need to make
the dictionary before the for loop as well. We have to check if the type is julia or burningshipjulia
to see if it needs cImag and cReal. We also have to make sure there are no repeats in the file.\
After we get dictionary items directly from the .frac files, I still need to calculate a few other
things. I will calculate miny, minx, maxx. I will use minx and maxx to find the pixelSize. Then
I'll add these all to the dictionary as well, so I can easily use them in ImagePainter.
If the given frac file name is "default frac", I will use a set-up dictionary to return.\
\
__FractalFactory.py :__ This is where we will call and create a Fractal. I need to figure out what
type of Fractal to make though, so I'll use if statements to decide. I need to pass in the fractalInfo
dictionary as the parameter, and I'll check the type using fractalInfo['type']. If the type is not one
of the three correct types, we will raise NotImplementedError. Then I will create the right
type of Fractal from there.\
\
__Fractal.py :__ This module will be an abstract class containing some dummy methods. I'll include
count() which is the most important. This one will accept a complex number and the max number of iterations
as a parameter and will return the number of iterations for a specific pixel. We need the max iteration
count so we know when to stop looking for a complex number greater than 2. I'll also use this
class to provide some details about the fractal. The ones we will still need are minx, miny, imageSize,
pixelSize when we paint the image in ImagePainter, so I'll make methods to return those but I'll make sure
that all my variables are private. I think I changed my mind and won't add minx, miny, maxx, pixelSize to
the dictionary. Instead I'll calculate it all in Fractal. \
\
__Julia.py :__ This will have the same stuff as Fractal.py except its count() method, which
will take the complex number and max iterations (which should be part of self) and will have a 
different formula. We'll name our complex number z and name another variable within the method c
which will be complex(-1,0). Then for the max number of iterations, will will do the formula
z = z * z + c until z is greater than z or until we run out of iterations. In either case, we'll 
return the iteration number where we stopped as the output for count.\
\
__Mandelbrot.py :__ This will be a concrete subclass of Fractal.py where we establish the count()
method with a complex number parameter that I'll name c. I'll also have a private variable z which
will be complex(0,0). Using these, we will use a for loop for the max number of iterations until
c is greater than 2 or until we reach the max iteration count. Either way, we'll return the iteration
number where we stopped.\
\
__Extra.py :__ We'll have a complex number as a parameter again and we'll have a new formula that
will repeat until the complex number is greater than 2 or until the for loop is finished. I don't know
what type of fractal we'll make yet.\
\
__PaletteFactory.py :__ This module will get information from FractalParser. The information only 
consists of the maximum number of iterations from the FractalInfo dictionary and the name of the
color scheme we'll be using, which is sys.argv[2] unless it's empty, then that parameter will be filled
by nothing. We can set a default argument for this parameter to be our default color scheme in case
nothing is provided. If it's not empty, we will check if it matches the name of one of my schemes.
If it does, we'll create that type of Palette object. If it's anything else, we'll raise NotImplementedErro
("Invalid gradient requested").\
\
__Palette.py :__ This will be a very minimal abstract class to provide structure and polymorphism
to the two concrete subclasses. It will have a getColor() method which will raise NotImplementedError
("Concrete subclass of Palette method must implement getColor() method") if called directly.
This method will take the iteration count provided by count() of Fractal as a parameter and will
return a color string in the form "#RRGGBB". We will also need the maximum number of iterations of
the fractal as a parameter so we can make an appropriate corresponding dynamic gradient. We will make
this gradient in the subclasses.\
\
__ColorScheme1.py :__ We will pick a few colors that we want to include in our images and then we will
use Color from the colour library to make a list of RGB string color values that range between the colors
we want. We can probably make a for loop to switch between the colors non-manually. We'll use the max 
iteration count to figure out how many shades we need between each color. We'll set up this list of
colors in the initializer __init__(dunder). Then the getColor() method will take the result 
of count() as its input and pop out one of the RGB value from the color list we just made based 
on its position.\
\
__ColorScheme2.py :__ This will be the same as ColorScheme1.py just with different colors.\
\
__ImagePainter.py :__ This one is a little tricky, because it has to get data from PaletteFactory
and FractalFactory. I think the methods I wrote in both of those and in Fractal should be very helpful.
I'll be using the data and methods previously set up to paint a picture. I'll need my Fractal object
because it can give me minx, miny, imageSize, and pixelSize. We will use those in a double for loop
that will iterate through every pixel. For each pixel, we'll formulate an x and y that will be the
complex number input for Fractal.count(). Then we'll get the color using the output of that for 
Palette.getColor(). Then we'll use photoImage.put to pair the resulting color with the specific 
pixel. After we do this for every row, we'll update the screen. We'll use TKinter to make a window
and print everything to the screen. We'll want to print the name of the file at the end as well.


## Phase 2: Design *(30%)*

```python
import sys

def main():
    if len(sys.argv) == 1:
        ImagePainter("default frac")
    elif len(sys.argv) == 2:
        ImagePainter(sys.argv[1])
    else:
        ImagePainter(sys.argv[1], sys.argv[2])

    # run ImagePainter
```
```python
def FractalParser(filename):
    infoTypes = {'type' : str,
                'pixels' : int,
                'centerx' : float,
                'centery' : float,
                'axisLength' : float,
                'iterations' : int,
                'creal' : float,
                'cimag' : float,}
    
    def main():
        FractalInfo = buildDictionary(filename)
        return FractalInfo
        
        ''' The following will be found in ImagePainter
        We build the dicitonary in FractalParser
        We create Palette and Fractal objects in ImagePainter using the factories
        
        fractal = FractalFactory.makeFractal(FractalInfo)
        palette = PaletteFactory.makePalette(FractalInfo['iterations'], palettename)'''
        
    def buildDictionary(filename):
        if filename == "default frac":
            # default FractalInfo dictionary
            return {'type' : 'mandelbrot',
                    'pixels' : 640,
                    'centerx' : -0.745,
                    'centery' : 0.105,
                    'axislength' : 0.01,
                    'iterations' : 384,}
        else:
            file = open(filename)
            tempDict = {}
            
        while True:
            line = file.readline()
            updateDictionary(line, tempDict)
            
            if not line:
                break
        
        file.close()
        return tempDict
            
    def updateDictionary(line, dict):
        if ":" in line:
            line.lower()
            # split, strip, and get rid of all spaces
            
            # if the key is valid and its corresponding data is valid, add it to the dictionary
            if line[0] in infoTypes and isCorrectType(line[1], infoTypes[line[0]]):
                dict.update({line[0] : line[1]})  # add line information to dictionary
    
            if dict['type'] == 'julia' and ('creal' and 'cimag' not in dict):
                raise NotImplementedError("Julia-type fractals must contain data for cReal and cImag")
                
    def isCorrectType(data, ofType):
        try:
            ofType(data)
            return True
        except ValueError:
            return False

    main()
```
```python
class FractalFactory:
    def __init__(self, fractalInfo):
        self.__FractalInfo = fractalInfo
        
        if self.__FractalInfo['type'] != 'julia' or 'mandelbrot' or 'extra':
            raise NotImplementedError("Unrecognized fractal type")
        
    def makeFractal(self):
        if self.__FractalInfo['type'] == 'julia':
            return Julia(self.__FractalInfo)
        elif self.__FractalInfo['type'] == 'mandelbrot':
            return Mbrot(self.__FractalInfo)
        else:
            return Extra(self.__FractalInfo)
```
```python
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
```
```python
class Julia(Fractal):
    def __init__(self, fractalInfo):
        super().__init__()
        self.__FractalInfo = fractalInfo

    def count(self, z):
        c = complex(-1, 0)

        for palette_index in range(self.__FractalInfo['iterations']):
            z = z * z + c
            if abs(z) > 2:
                return palette_index

        return self.__FractalInfo['iterations'] - 1
    
    def getImageSize(self):
        super().getImageSize()
    
    def getMinX(self):
        super().getMinX()
        
    def getMinY(self):
        super().getMinY()
        
    def getPixelSize(self):
        super().getPixelSize()
```
```python
class Mbrot(Fractal):
    def __init__(self, fractalInfo):
        super().__init__()
        self.__FractalInfo = fractalInfo

    def count(self, c):
        z = complex(0, 0)

        for palette_index in range(self.__FractalInfo['iterations']):
            z = z * z + c
            if abs(z) > 2:
                return palette_index

        return self.__FractalInfo['iterations'] - 1
    
    def getImageSize(self):
        super().getImageSize()
    
    def getMinX(self):
        super().getMinX()
        
    def getMinY(self):
        super().getMinY()
        
    def getPixelSize(self):
        super().getPixelSize()
```
```python
class Extra(Fractal):
    def __init__(self, fractalInfo):
        super().__init__()
        self.__FractalInfo = fractalInfo

    # everything commented out in this method needs to be decided later
    def count(self, complexNum):  # decide what this is later
        # z = complex(0, 0)

        for palette_index in range(self.__FractalInfo['iterations']):
            # z = z * z + c
            if abs(z) > 2:
                return palette_index

        return self.__FractalInfo['iterations'] - 1
    
    def getImageSize(self):
        super().getImageSize()
    
    def getMinX(self):
        super().getMinX()
        
    def getMinY(self):
        super().getMinY()
        
    def getPixelSize(self):
        super().getPixelSize()
```
```python
class PaletteFactory():
    def __init__(self, maxIterations, palettename = "ColorScheme1"):
        self.__maxIter = maxIterations
        self.__palette = palettename
        
        if self.__palette != ("ColorScheme1" or "ColorScheme2"):
            raise NotImplementedError("Invalid gradient requested")
        
    def makePalette(self):
        if self.__palette == "ColorScheme1":
            return ColorScheme1(self.__maxIter)
        else:
            return ColorScheme2(self.__maxIter)
```
```python
class Palette:
    def __init_(self, maxIterations):
        self.__maxIter = maxIterations
        
    def getColor(self, count):
        raise NotImplementedError("Concrete subclass of Palette method must implement getColor() method")
```
```python
from colour import Color

class ColorScheme1(Palette):
    def __init_(self, maxIterations):
        super().__init()
        self.__maxIter = maxIterations
        
    def getColor(self, count):
        super().__init()
        colors = []  # list of colors i want in my palette
        palette = []  # list of RGB gradient between colors list
        
        for i in range(len(colors) - 1):
            start = Color(colors[i])
            end = colors[i + 1]
            
            # i'm not sure if the below line will work so I'll write the pseudocode to show my intentions
            # palette.append([c.hex_l for c in start.range_to(end, self.__maxIter // len(colors))])
            # for c in start.range_to(end, self.__maxIter // len(colors)):
                # palette.append(c.hex_l)
            for c in range(from start to end, making enough colors for self.__maxIter // len(colors)):
                palette.append(RGB for c)
            
        return palette[count]
```
```python
class ColorScheme2(Palette):
    # will be the same as ColorScheme1 except for colors list in getColor()
```
```python
from tkinter import Tk, Canvas, PhotoImage, mainloop

def ImagePainter(filename, palettename):
    FractalInfo = FractalParser(filename)
    fractal = FractalFactory.makeFractal(FractalInfo)
    palette = PaletteFactory.makePalette(FractalInfo['iterations'], palettename)
    
    window = Tk()
    image = PhotoImage(width=fractal.getImageSize(), height=fractal.getImageSize())
    
    # create image
    # display initial image before color
    
    for row in range(FractalInfo['imageSize'], 0, -1):
        for col in range(FractalInfo['imageSize']):
            x = FractalInfo['minx'] + col * FractalInfo['pixelSize']
            # OR: x = fractal.getMinX() + col * fractal.getPixelSize()
            y = FractalInfo['miny'] + row * FractalInfo['pixelSize']
            # OR: y = fractal.getMinY() + row * fractal.getPixelSize()
            color = palette.getColor(fractal.count(complex(x, y)))
            # put color in image
        window.update()
        
    mainloop()
```

## Phase 3: Implementation *(15%)*

When I moved all my pseudocode from my Plan to the actual modules, I didn't realize that 
having some non-object-oriented modules wouldn't work. So I had to convert FractalParser
and ImagePainter to classes instead of just methods. I also forgot to actually convert the
data in the dictionaries to the correct type, so they were all in there as strings. I also
accidentally made part of the axislength key uppercase, so it excluded axislength from
all dictionaries until I found the error. I also didn't realize that you have to return
the superclass version of a method instead of just call it if it's the type of method with
a return value. If you don't do that it will return a NoneType object.\
\
I really struggled with making the color palette as well. I couldn't figure out how to use
the range_to function or how to make the palette the exact right length. I had to use integer
division and mod to fill in the gaps and make it all even.\
\
I also ended up restructuring my program a little as I read through the assignment
instructions again. My ImagePainter was a little messed up, but I fixed it and updated
my UML accordingly.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

* A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
* Write your test cases in plain language such that a non-coder could run them and replicate your experience.

I forgot to add a few error messages. If a certain type of necessary data was missing, I added
an error message. I also had to add an error if the necessary data name is there, but the
corresponding data is missing. 


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

* Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
* Fill out the Assignment Reflection on Canvas.

* Pretty much the entirety of Fractal Parser is very sloppy.
* I'm not sure how the math of the fractals works or the tkinter parts.
* I think it might take me a minute because I put error messages and collected things in weird places.
* My documentation is pretty thorough so I think it'll make sense to me and anyone else at any time.
* It should be decently easily because my program is object-oriented.
* Updates might be hard. I see tkinter struggling.
