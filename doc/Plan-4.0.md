# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

* A detailed written description of the problem this program aims to solve.
* Describe what a *good* solution looks like.
    * List what you already know how to do.
    * Point out any challenges that you can foresee.

In this sprint, I will refactor the existing code in main.py, julia_fractal.py, and
mbrot_fractal.py. A good solution to this issue will be very readable code with all
the useless bits removed. I'll try and make the program as multi-functional as 
possible. This will include lots of well-named functions and parameters. I'll make sure
to have any "magic numbers" labeled with all-caps so anyone reading my code will
understand what they mean and that they don't change. I'll look for unnecessary global
variables as well. I'll have to double-check every cluster of code to figure out what
it's doing and if the corresponding comment is lying to me or not. I want to create
functions based on their purpose. This way it's easy to name and easy to keep track of.
I will look for repeated groups of code because those might be able to be made into
functions as well. They also might be useless. I guess I'll just have to go through the
code very slowly and very thoroughly like I did in Bingo Card Generator. When I read
through that, I found a bug before even re-reading the instructions where it said there
was a bug in the starter code. I think I'll have trouble figuring out what to put into
make into classes, because I feel like I haven't worked with classes enough or made my
own to the point where I'm comfortable understanding what should be separated in that
way. 


## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

When the program is run from the command line, you put in src/main.py and then the name of the
fractal you want to draw. If there are not enough arguments, it will return an error and show you
all the possible fractals you can draw. If there are too many arguments, it will just accept
the first command after src/main.py to draw. If that argument is not one of the options, we will
again return the list of possible fractal options. I have figured out that in the mbrot file,
the palette contains a bunch of colors. As many colors as there are, that's how many times
the complicated math will run. Once that math reaches 2 or higher, the iterations will stop and
whatever iteration we landed on will correspond to the color from the palette that we
choose. I took out everything that was commented out already, because it doesn't affect the code
at all if it's not working right now. I also got rid of the variables that were color names and
had the value of RGB colors. They weren't doing much besides taking up space, so I transferred
them directly into the palette list in mbrot_fractal.py. I changed the name of the dictionaries
holding the fractal names and properties to "shapes", because there are a lot of places where "image"
or "img" is the variable name. "Images" is way too close to make sense. I started to realize that
mbrot_fractal and julia_fractal each had three main functions. There was the main function that
gets run from main.py. Then there is the getPixelColor which I manipulated so that they
are both built the same, with parameter input of an integer (either z or c) and the list of palette
colors. That leaves paint from mbrot_fractal and makeFractal from julia_fractal to be the same but
they have quite different structures. After Smell 31, the code was mostly cleaned up and I had to 
restructure from there. Main and makeFractal were exactly the same so I just copied the functions
from Julia to MBot because Julia had more usable parameters.


## Phase 2: Design *(30%)*

**Deliver:**

* Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
* Pseudocode that captures how each function works.
    * Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    * Explain what happens in the face of good and bad input.
    * Write a few specific examples that occurred to you.

I did most of this in Smells.md but I'll just write some of the functions below.

```python
def main(imageArg):
    get before time
    set up the window
    set up the image
    makeFractal
    get after time
    print(number of seconds it took to print the file imageArg)
    
    pass the output to a file named imageArg
    print("wrote picture")
    print("close the window to exit")
    loop again
```
```python
def makeFractal():
    find minx using the center and length of axis
    find maxx using the center and length of axis
    find miny using the center and length of axis
    
    get pixel size using maxx, minx, and size of image
    
    initialize a canvas
    pack the canvas
    create image on canvas
    
    for row in range(size of image, 0, -1):
        for col in range(size of image):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            color = getPixelColor
            put the pixel in the image
        update the window to print the row
```
```python
def getPixelColorMBrot():
    z = complex(0,0)
    for color in colors:
        update z
        if z > 2:
            return color
    return colors[-1]
```
```python
def getPixelColorJulia():
    c = complex(-1,0)
    for color in colors:
        update c
        if z > 2:
            return color
    return colors[-1]
```


## Phase 3: Implementation *(15%)*

**Deliver:**

* (More or less) working code.
* Note any relevant and interesting events that happened while you wrote the code.
    * e.g. things you learned, things that didn't go according to plan

Pretty much everything went according to plan. I didn't realize how the code relied on the
order of the palette. Everything else was pretty simple but meticulous refactoring.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

I struggled getting rid of some of the global variables, especially global window and global
win until I added parameters. I also had to figure out how best to describe some of the variables
that were very similar or poorly named. I also deleted a lot of unnecessary variables. My 
biggest issue was how long it took to break down the files one by one until it was in its 
simplest form.


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

* I think there's probably a better way to break up my files into methods and classes so that I can refactor them more quickly.
* I don't understand how the for loop with z = z * z + c work. They just do I suppose. Also, I've never worked with the canvas or printing images to a screen. I kind of just trusted the starter code for that.
* It wouldn't take me too long to find a bug unless it was with some of the new libraries, like TKinter.
* My documentation in Smells is pretty thorough but the line numbers probably aren't right anymore because I implemented as I worked.
* I'll probably remember most of the problems I had once I look at this again in six months.
* Adding a new feature may be tricky but I'll have to make sure to even it out between Julia and MBrot.
* The interactions probably won't change much between hardware, OS's, and versions of Python. I'm thinking my code will work quite similarly except for TKinter.