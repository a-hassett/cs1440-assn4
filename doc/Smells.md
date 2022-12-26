# Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
*	Copy the offensive code
*	Explain why the smell is a problem
*	Describe how you can fix


### These are some of the code smells you may find in the starter code:

0.  "Magic" numbers
    *   Numeric literals that appear in critical places but without any apparent meaning
    *   "When I see the number `214` here, does it have the same meaning as the `214` over there?"
1.  Global variables
    *   A global is being used to avoid passing a parameter into a function
    *   A global is being used to return an extra value from a function
2.  Poorly-named variables
    *   Variables with one-letter long names are okay to use in special contexts; otherwise, they should be avoided
        *   For example, a counter called `i` or `j` used in a `for` loop that is but a few lines long
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
    *   Variables with really, really long names can make code *less* easy to read
    *   If a programmer is not careful, variables can accidentally override or "shadow" other identifiers in a program
        *   Builtin Python functions such as `input`, `len`, `list`, `max`,
            `min` and `sum` are especially susceptible to this
    *   Variable names should strike a good balance between brevity and descriptiveness
3.  Comments that share too much information
    *   A function or method is filled with many explanatory comments
    *   This is often done because the variable names and function names are poorly chose
    *   Rather, let the code speak for itself
4.  Comments that lie to you
    *   A comment which may have once been helpful, but no longer accurately describes the code
    *   A comment that is straight-up misleading, perhaps written by a developer without a clue
5.  Parameter list that is too long
    *   More than three or four parameters for a method
    *   Parameters that are passed in but left unused
6.  Function/Method that is too long
    *   A method contains too many lines of code
    *   Typically this happens because the method has too many different responsibilities
    *   Generally, any method longer than ten lines should make you ask the question "what if I split this into smaller, more focused pieces?"
7.  Overly complex decision trees
    *   Overly long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Have all of the branches been tested?
8.  Spaghetti code
    *   Lots of meandering code without a clear goal
    *   Many functions/objects used in inconsistent ways
    *   All code is contained in one giant function/method with huge `if/else` branches
    *   "It would be easier to rewrite this than to understand it"
9.  Redundant code
    *   When you see a line of code that is repeated, ask whether it makes any difference to be run more than once.
10. Dead code
    *   A variable, parameter, field, method or class is no longer used (usually because it is obsolete)
    *   Big blocks of commented-out code that serve no purpose and clutter up the file

Other code smells may be present; list them as well.

## Code Smells

*TODO: Write your report here*

0. `src/main.py`, [lines 44-51]\
   * [What kind of code smell is this?] Redundant code
   * [Why is the smell a problem?] There's an easier way to do this without making a new variable to list all the options
   * Code Snippet:
     ```python
     elif sys.argv[1] not in JULIAS + MBROTS:  	         	  
         print(f"ERROR: {sys.argv[1]} is not a valid fractal")  	         	  
         print("Please choose one of the following:")  	         	  
         all_of_the_fractals = JULIAS  	         	  
         all_of_the_fractals.extend(MBROTS)  	         	  
         for i in all_of_the_fractals:  	         	  
             print(f"\t{i}")  	         	  
         sys.exit(1)  	
     ```
   * How the code smell was fixed:
     ```python
     elif sys.argv[1] not in JULIAS + MBROTS:  	         	  
         print(f"ERROR: {sys.argv[1]} is not a valid fractal")  	         	  
         print("Please choose one of the following:")	         	  
         for i in JULIAS + MBROTS:  	         	  
             print(f"\t{i}")  	         	  
         sys.exit(1)  	
     ```
   * [Explain what you changed] I had the for loop just run through JULIAS and MBROTS instead of it making a variable to collect them both.


1. `src/main.py`, [lines 29-30]\
   * [What kind of code smell is this?] Readability
   * [Why is the smell a problem?] If I'm making the julia_fractal file name more readable, I might as well do the same to the mbrot_fractal file.
   * Code Snippet:
     ```python	
     import julia_fractal as julia  	         	  
     import mbrot_fractal
     ```
   * How the code smell was fixed:
     ```python
     import julia_fractal as julia  	         	  
     import mbrot_fractal as mbrot	
     ```
   * [Explain what you changed] I'm making the name we use to call mbrot_fractal.py more readable for my sanity's sake.


2. `src/main.py`, [lines 53-61]\
   * [What kind of code smell is this?] Lying comment. Redundant code.
   * [Why is the smell a problem?] The code doesn't quit here. It decides whether to use the mbrot file or the julia file. We also don't need to identify sys.argv[1] as the fractal name, especially when we don't even end up using it consistently.
   * Code Snippet:
     ```python	
     # Otherwise, quit with an error message to help the user learn how to run it  	         	  
     else:  	         	  
        # fractal is the 1st argument after the program name  	         	  
        fracal = sys.argv[1]  	         	  
        if sys.argv[1] in JULIAS:  	         	  
            julia.julia_main(sys.argv[1])  	         	  
        elif sys.argv[1] in MBROTS:  	         	  
            fratcal = sys.argv[1]  	         	  
            mbrot_fractal.mbrot_main(fratcal)  
     ```
   * How the code smell was fixed:
     ```python
     # Otherwise, the command line input is correct and we can continue 	         	  
     else:  
        fractal = sys.argv[1]	         	  
        if fractal in JULIAS:  	         	  
            julia.julia_main(fractal)  	         	  
        elif fractal in MBROTS:  	         	  
            mbrot.mbrot_main(fractal) 	
     ```
   * [Explain what you changed] I decided to keep the fractal variable because it's more readable, but I actually used it to check which python code to continue with and passed the fractal name as the parameter. I think I'll also end up changing the names of the main functions in both to just "main" plus parameters so it's less redundant.


3. `src/mbrot_fractal.py`, [lines 52-68]\
   * [What kind of code smell is this?] Redundant code
   * [Why is the smell a problem?] It has tons of repeat colors, which defeats a lot of the purpose
   * Code Snippet:
     ```python
     #palette = [LIME_GREEN, '#a8f71b', '#c0ef34', '#d2ea4c', '#dfe563', '#e2db78',  	         	  
     #        '#e0d28d', '#dfce9f', '#e0ceb1', '#e2d2c1', '#e5d9d0', '#eae1de',  	         	  
     #        '#efebea', '#f7f5f5', WHITE, '#f7f5f5', '#efebea', '#eae0de',  	         	  
     #        '#e5d6d0', '#e2cdc1', '#e0c5b1', '#dfbf9f', '#e0bc8d', '#e2bd78',  	         	  
     #        '#e5c163', '#eac94c', '#efd634', '#f7e81b', LEMON, '#f7e81b',  	         	  
     #        '#efd634', '#eac94c', '#e5c163', '#e2bd78', '#e0bc8d', '#dfbf9f',  	         	  
     #        '#e0c5b1', '#e2cdc1', '#e5d6d0', '#eae0de', '#efebea', '#f7f5f5',  	         	  
     #        WHITE, '#f6f5f5', '#efeaea', '#e9dfdd', '#e4d4d0', '#e1c9c1',  	         	  
     #        '#dfbfb0', '#deb69f', '#deae8c', '#e0a978', '#e2a563', '#e7a54c',  	         	  
     #        '#eca834', '#f3ae1b', TANGERINE, '#f3ae1b', '#eca834', '#e7a54c',  	         	  
     #        '#e2a563', '#e0a978', '#deae8c', '#deb69f', '#dfbfb0', '#e1c9c1',  	         	  
     #        '#e4d4d0', '#e9dfdd', '#efeaea', '#f6f5f5', WHITE, '#f6f6f5',  	         	  
     #        '#efefea', '#e5e9de', '#d5e3d1', '#c3dfca', '#b4ddd1', '#a3d2db',  	         	  
     #        '#91adda', '#857fdb', '#a66bdc', '#dc56df', '#e33f9d', WHITE,  	         	  
     #        '#f6f5f4', '#eeeee8', '#e2e7db', '#cedead', '#beefcc', '#abdbd9',  	         	  
     #        '#99beda', '#858cda', '#9c70dc', '#d159de', '#e341a4',  	         	  
     #        GRAPEFRUIT_PINK, ]  
     ```
   * How the code smell was fixed:
   ```python
    # palette = [LIME_GREEN, '#a8f71b', '#c0ef34', '#d2ea4c', '#dfe563', '#e2db78',  	         	  
    #        '#e0d28d', '#dfce9f', '#e0ceb1', '#e2d2c1', '#e5d9d0', '#eae1de',  	         	  
    #        '#efebea', '#f7f5f5', WHITE, '#eae0de',  	         	  
    #        '#e5d6d0', '#e2cdc1', '#e0c5b1', '#dfbf9f', '#e0bc8d', '#e2bd78',  	         	  
    #        '#e5c163', '#eac94c', '#efd634', '#f7e81b', LEMON,  	         	  
    #        	         	  
    #       	         	  
    #        '#f6f5f5', '#efeaea', '#e9dfdd', '#e4d4d0', '#e1c9c1',  	         	  
    #        '#dfbfb0', '#deb69f', '#deae8c', '#e0a978', '#e2a563', '#e7a54c',  	         	  
    #        '#eca834', '#f3ae1b', TANGERINE,	         	  
    #        	         	  
    #        '#f6f6f5',  	         	  
    #        '#efefea', '#e5e9de', '#d5e3d1', '#c3dfca', '#b4ddd1', '#a3d2db',  	         	  
    #        '#91adda', '#857fdb', '#a66bdc', '#dc56df', '#e33f9d',  	         	  
    #        '#f6f5f4', '#eeeee8', '#e2e7db', '#cedead', '#beefcc', '#abdbd9',  	         	  
    #        '#99beda', '#858cda', '#9c70dc', '#d159de', '#e341a4',  	         	  
    #        GRAPEFRUIT_PINK] 	
    ```
   * [Explain what you changed] I took out all of the repeat colors.


4. `src/mrbot_fractal.py`, [lines 70-87]\
   * [What kind of code smell is this?] Lying comment. Redundant code.
   * [Why is the smell a problem?] The color palette contains 112 total colors, not 100. Also, there are repeats. I'm gonna see if there are actually 100 after removing repeats.
   * Code Snippet:
     ```python	
     # This color palette contains 100 color steps.  	         	  
     palette = [  	         	  
     '#89ff00', '#a4f817', '#baf12e', '#ccec43', '#d9e758', '#e3e46b', '#e1d97e',  	         	  
     '#e0d18f', '#dfce9f', '#e0ceaf', '#e1d1bd', '#e4d6cb', '#e7ddd7', '#ece5e3',  	         	  
     '#f1eeed', '#f8f7f7', WHITE, '#f8f7f7', '#f1eeed', '#ece4e3', '#e7dbd7',  	         	  
     '#e4d3cb', '#e1cbbd', '#e0c4af', '#dfbf9f', '#e0bd8f', '#e1bc7e', '#e4bf6b',  	         	  
     '#e7c458', '#eccd43', '#f1da2e', '#f8eb17', LEMON, '#f8eb17', '#f1da2e',  	         	  
     '#eccd43', '#e7c458', '#e4bf6b', '#e1bc7e', '#e0bd8f', '#dfbf9f', '#e0c4af',  	         	  
     '#e1cbbd', '#e4d3cb', '#e7dbd7', '#ece4e3', '#f1eeed', '#f8f7f7', WHITE,  	         	  
     '#f7f6f6', '#f1eded', '#ebe4e2', '#e6dad7', '#e3d0ca', '#e0c6bd', '#debeae',  	         	  
     '#deb69f', '#deaf8e', '#dfaa7d', '#e1a66b', '#e4a557', '#e9a643', '#eea92e',  	         	  
     '#f4af17', TANGERINE, '#f4af17', '#eea92e', '#e9a643', '#e4a557', '#e1a66b',  	         	  
     '#dfaa7d', '#deaf8e', '#deb69f', '#debeae', '#e0c6bd', '#e3d0ca', '#e6dad7',  	         	  
     '#ebe4e2', '#f1eded', '#f7f6f6', WHITE, '#f8f7f7', '#f2f1ef', '#ebece5',  	         	  
     '#e2e7db', '#d3e3d0', '#c5e0ca', '#b9ddce', '#abdbd9', '#9ec8da', '#8fa7da',  	         	  
     '#8480db', '#9c70dc', '#c25fde', '#e04dcb', '#e43b8d', WHITE, '#f7f6f6',  	         	  
     '#f0efec', '#e8eae1', '#dae5d5', '#c8e1cb', '#badecd', '#abdbd9', '#9cc4da',  	         	  
     '#8b9cda', '#8d79db', '#b066dd', '#e052da', '#e33e97', GRAPEFRUIT_PINK, ]  	
     ```
   * How the code smell was fixed:
     ```python
     # This color palette contains 100 color steps.  	         	  
     palette = [  	         	  
     '#89ff00', '#a4f817', '#baf12e', '#ccec43', '#d9e758', '#e3e46b', '#e1d97e',  	         	  
     '#e0d18f', '#dfce9f', '#e0ceaf', '#e1d1bd', '#e4d6cb', '#e7ddd7', '#ece5e3',  	         	  
     '#f1eeed', '#f8f7f7', WHITE, '#f8f7f7', '#ece4e3', '#e7dbd7',  	         	  
     '#e4d3cb', '#e1cbbd', '#e0c4af', '#dfbf9f', '#e0bd8f', '#e1bc7e', '#e4bf6b',  	         	  
     '#e7c458', '#eccd43', '#f1da2e', '#f8eb17', LEMON,	         	  
       	  
     '#f8f7f7', 	         	  
     '#f7f6f6', '#f1eded', '#ebe4e2', '#e6dad7', '#e3d0ca', '#e0c6bd', '#debeae',  	         	  
     '#deb69f', '#deaf8e', '#dfaa7d', '#e1a66b', '#e4a557', '#e9a643', '#eea92e',  	         	  
     '#f4af17', TANGERINE,         	  
        	  
     '#f2f1ef', '#ebece5',  	         	  
     '#e2e7db', '#d3e3d0', '#c5e0ca', '#b9ddce', '#abdbd9', '#9ec8da', '#8fa7da',  	         	  
     '#8480db', '#9c70dc', '#c25fde', '#e04dcb', '#e43b8d',  	         	  
     '#f0efec', '#e8eae1', '#dae5d5', '#c8e1cb', '#badecd', '#9cc4da',  	         	  
     '#8b9cda', '#8d79db', '#b066dd', '#e052da', '#e33e97', GRAPEFRUIT_PINK]	
     ```
   * [Explain what you changed] Turns out there are many less than 100 colors here. I'm not really sure what that implies, but I'll keep an eye out.


5. `src/mrbot_fractal.py`, [lines 234-238]\
   * [What kind of code smell is this?] Redundant code
   * [Why is the smell a problem?] It lists the parameters for the spiral1 image twice, so it's unnecessary.
   * Code Snippet:
     ```python	
     'spiral1': {  	         	  
            'centerX': -0.747,  	         	  
            'centerY': 0.1075,  	         	  
            'axisLen': 0.002,  	         	  
            },
     ```
   * How the code smell was fixed:
     ```python
     #delete whole section
     ```
   * [Explain what you changed] Get rid of all of it. We already have that same exact code like 10 lines above it.


6. `src/mrbot_fractal.py`, [lines 94, 131-136, 260-261]\
   * [What kind of code smell is this?] Global variables
   * [Why is the smell a problem?] We use the global variable image in multiple places instead of just passing it into the parameters of a function when they are called.
   * Code Snippet:
     ```python	
     img = None
     
     #...
     
     def paint(fractals, imagename):  	         	  
     """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
     This code creates an image which is 640x640 pixels in size."""  	         	  

        global palette  	         	  
        global img 
     
     #...
     
     def mbrot_main(image):
        global img 
      
     ```
   * How the code smell was fixed:
     ```python
     def paint(fractals, imagename, img):  	         	  
     """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
     This code creates an image which is 640x640 pixels in size."""  	         	  

        global palette
     
     #...
     
     def mbrot_main(image, img):
        img = PhotoImage(width=512, height=512)  	         	  
        paint(images, image, img)  	
     ```
   * [Explain what you changed] I put img as parameters in all the functions where it included img as a global variable.


7. `src/mrbot_fractal.py`, [line 260]
   * [What kind of code smell is this?] Readability
   * [Why is the smell a problem?] I'd rather the function be name "main" because it's only called once in main.py and it has "mbrot" in front anyway, so there's no need to specify that.
   * Code Snippet:
     ```python	
     def mbrot_main(image):
     ```
   * How the code smell was fixed:
     ```python
     def main(image):
     ```
   * [Explain what you changed] I changed the name of the main function in mbrot_fractal.py.


8. `src/julia_fractal.py`, [line 264]
   * [What kind of code smell is this?] Readability
   * [Why is the smell a problem?] I'd rather the function be name "main" because it's only called once in main.py and it has "julia" in front anyway, so there's no need to specify that.
   * Code Snippet:
     ```python	
     def julia_main(image):
     ```
   * How the code smell was fixed:
     ```python
     def main(image):
     ```
   * [Explain what you changed] I changed the name of the main function in julia_fractal.py.


9. `src/mbrot_fractal.py`, [line 177-225]
   * [What kind of code smell is this?] Cohesion
   * [Why is the smell a problem?] Main.py lists the mbrot fractals in alphabetical order, and I want mbrot_fractal to follow the same pattern.
   * Code Snippet:
     ```python	
     images = {  	         	  
        'mandelbrot': {},  	         	  
        'mandelbrot-zoomed': {},  	         	  
        'spiral0': {},  	         	  
        'spiral1': {},  	         	  
        'seahorse': {},
        'elephants': {},  	         	  
        'leaf': {},  	         	  
        'starfish': {},  	         	  
        }
     ```
   * How the code smell was fixed:
     ```python
     shapes = {
        'elephants': {},  	         	  
        'leaf': {},  
        'mandelbrot': {},  	         	  
        'mandelbrot-zoomed': {},
        'seahorse': {},
        'spiral0': {},  	         	  
        'spiral1': {},	         	  
        'starfish': {} 	         	  
        }
     ```
   * [Explain what you changed] I simply changed the order of the dictionary so the name of the mbrot fractals would be alphabetical.


10. `src/julia_fractal.py`, [line 177-225]
    * [What kind of code smell is this?] Cohesion
    * [Why is the smell a problem?] Main.py lists the julia fractals in alphabetical order, and I want mbrot_fractal to follow the same pattern. I also want the dictionary to have a more descriptive name.
    * Code Snippet:
      ```python	
      f = {  	         	  
         # The full julia set  	         	  
         'fulljulia': {},  	         	  

         # This one looks like an hourglass to me  	         	  
         'hourglass': {},  	         	  

         # This fractal reminds me of lakes, but it might remind somebody else of something else  	         	  
         'lakes': {},  	         	  

         # My grandmother has lace curtains that look JUST LIKE THIS!  	         	  
         'lace-curtains': {},  	         	  
      }
      ```
    * How the code smell was fixed:
      ```python
      shapes = {  	         	  
         'fulljulia': {},	         	  
         'hourglass': {},  	         	  
         'lace-curtains': {}, 	         	  
         'lakes': {}    	         	  
      }
      ```
    * [Explain what you changed] I simply changed the order of the dictionary so the name of the mbrot fractals would be alphabetical. I also took out the distracting comments that weren't contributing anything. I also changed the name of the dictionary to match that of mbrot. I find it more descriptive.


11. `src/mbrot_fractal.py`, [line 23, 64, 72-81, 136]\
    * [What kind of code smell is this?] Global variable, double declare, redundancy
    * [Why is the smell a problem?] The global variable is less readable and controllable, the double declaration of MAX_ITERATIONS is unnecessary, we don't need to make a variable for the length when max_iter is the same.
    * Code Snippet:
      ```python	
      MAX_ITERATIONS = -1 
      
      #...
      
      MAX_ITERATIONS = len(palette)
      
      #...
      
      def colorOfThePixel(c, palette):  	         	  
         """Return the color of the current pixel within the Mandelbrot set"""  	         	  
         global z  	         	  
         z = complex(0, 0)  # z0  	         	  

         global MAX_ITERATIONS  	         	  
         global iter  	         	  

         len = MAX_ITERATIONS
         for iter in range(len):
      
      #...
      
      color = colorOfThePixel(complex(x, y), palette)
      ```
    * How the code smell was fixed:
      ```python
      MAX_ITERATIONS = len(palette)
      
      #...
      
      def colorOfThePixel(c, palette, max_iter):  	         	  
         """Return the color of the current pixel within the Mandelbrot set"""  	         	  
         global z  	         	  
         z = complex(0, 0)  # z0  	         	  
  	         	  
         global iter  	         	  

         for iter in range(max_iter):
      
      #...
      
      color = colorOfThePixel(complex(x, y), palette, MAX_ITERATIONS)
      ```
    * [Explain what you changed] I kept MAX_ITERATIONS as a global variable, but I won't treat it as such when it's in colorOfThePixel. Instead, I give that function the max iterations as a parameter. Then we use that parameter as the number of for loop iterations. We also have to update where colorOfThePixel gets used with the new extra parameter.


12. `src/mbrot_fractal.py`, [lines 95-97]
    * [What kind of code smell is this?] Redundancy
    * [Why is the smell a problem?] There are two return statements right next to each other with no differentiating condition. The second return statement will never be reached, and it will be out of range of index.
    * Code Snippet:
    ```python
    # XXX: one of these return statements made the program crash...
    return palette[MAX_ITERATIONS - 1]   # Indicate a bounded sequence  	         	  
    return palette[MAX_ITERATIONS]
    ```
    * How the code smell was fixed:
    ```python
    # return corresponding color from palette depending on iterations to get to 2
    return palette[MAX_ITERATIONS - 1]
    ```
    * [Explain what you changed] I removed the second return statement.


13. `src/mbrot_fractal.py`, [line 71]
    * [What kind of code smell is this?] Naming conventions
    * [Why is the smell a problem?] The name of the function is really long and it could be shorter and more standardized.
    * Code Snippet:
    ```python
    def colorOfThePixel(c, palette, max_iter):
    ```
    * How the code smell was fixed:
    ```python
    def getPixelColor(c, palette, max_iter):
    ```
    * [Explain what you changed] I just changed the name of the function and nothing else. I will also have to update anywhere that uses the function.


14. `src/mbrot_fractal.py`, [lines 93-94]
    * [What kind of code smell is this?] Dead code
    * [Why is the smell a problem?] It's useless lines of code.
    * Code Snippet:
    ```python
    else:
        pass
    ```
    * How the code smell was fixed:
    ```python
    # delete this section
    ```
    * [Explain what you changed] I just took out the lines of code that said that if none of the interesting conditions are met, do nothing. We don't need code that tells the computer to do nothing.


14. `src/mbrot_fractal.py`, [lines 95]
    * [What kind of code smell is this?] Over-complication
    * [Why is the smell a problem?] It's harder to understand where things are coming from when they use lots of variables, especially when unnecessary.
    * Code Snippet:
    ```python
    return palette[MAX_ITERATIONS - 1]
    ```
    * How the code smell was fixed:
    ```python
    return palette[-1]
    ```
    * [Explain what you changed] The point of this line is to return the last item in the palette. Using the -1 index is easier and more understandable for other coders.


15. `src/mbrot_fractal.py`, [lines 64, 73-74]
    * [What kind of code smell is this?] Global variables
    * [Why is the smell a problem?] We reset the value of z anyway everywhere we use it, so it doesn't need to have a global value.
    * Code Snippet:
    ```python
    z = 0
    
    #...
    
    global z  	         	  
    z = complex(0, 0)  # z0
    ```
    * How the code smell was fixed:
    ```python
    z = complex(0, 0)  # z0
    ```
    * [Explain what you changed] I got rid of the global-ness of z.

16. `src/mbrot_fractal.py`, [lines 63, 70-75]
    * [What kind of code smell is this?] Global variables
    * [Why is the smell a problem?] It's creating unnecessary complication.
    * Code Snippet:
    ```python
    MAX_ITERATIONS = len(palette)
    
    #...
    
    def getPixelColor(c, palette, max_iter):
    """Return corresponding color from palette depending on iterations to get to 2"""

    z = complex(0, 0)  # z0

    for iter in range(max_iter):
    ```
    * How the code smell was fixed:
    ```python
    def getPixelColor(c, palette):
    """Return corresponding color from palette depending on iterations to get to 2"""

    z = complex(0, 0)  # z0
    max_iterations = len(palette)

    for iter in range(max_iterations):
    ```
    * [Explain what you changed] I got rid of the global variable MAX_ITERATIONS because everywhere it was used, it could have been produced more organically there.


17. `src/mbrot_fractal.py`, [lines 63, 83-89]
    * [What kind of code smell is this?] Dead code
    * [Why is the smell a problem?] It's creating unnecessary complication and confusion. There's no need to have code just for the fun of it. It just slows down the runtime.
    * Code Snippet:
    ```python
    seven = 7.0
    
    #...
    
    elif abs(z) > seven:  	         	  
        print("You should never see this message in production")  	         	  
        continue  	         	  
        break 	         	  
    elif abs(z) < 0:  	         	  
        print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={max_iter}")
        sys.exit(1)
    elif abs(z) < TWO:  	         	  
        itcontinue
    ```
    * How the code smell was fixed:
    ```python
    # delete this section
    ```
    * [Explain what you changed] If the absolute value of z is greater than seven, nothing happens. The absolute value will never be less than 0 due to the definition of absolute value. Also, the seven variable is only used here, so I will get rid of it as well.


18. `src/mbrot_fractal.py`, [lines 19-61]
    * [What kind of code smell is this?] Redundancy. Lying comment.
    * [Why is the smell a problem?] It's hard to look at. Plus, we don't have a need to understand what colors are in the palette list, given that there are around 100 that we don't know in it already.
    * Code Snippet:
    ```python
    GRAPEFRUIT_PINK = '#e8283f'  	         	  
    LEMON = '#fdff00'  	         	  
    LIME_GREEN = '#89ff00'  	         	  
    KUMQUAT = '#fac309'
    POMELLO = '#2fff00'  	         	  
    TANGERINE = '#f7b604'  	         	  
    WHITE = '#ffffff'  	         	  
    #palette = [LIME_GREEN, '#a8f71b', '#c0ef34', '#d2ea4c', '#dfe563', '#e2db78',  	         	  
    #        '#e0d28d', '#dfce9f', '#e0ceb1', '#e2d2c1', '#e5d9d0', '#eae1de',  	         	  
    #        '#efebea', '#f7f5f5', WHITE, '#f7f5f5', '#efebea', '#eae0de',  	         	  
    #        '#e5d6d0', '#e2cdc1', '#e0c5b1', '#dfbf9f', '#e0bc8d', '#e2bd78',  	         	  
    #        '#e5c163', '#eac94c', '#efd634', '#f7e81b', LEMON, '#f7e81b',  	         	  
    #        '#efd634', '#eac94c', '#e5c163', '#e2bd78', '#e0bc8d', '#dfbf9f',  	         	  
    #        '#e0c5b1', '#e2cdc1', '#e5d6d0', '#eae0de', '#efebea', '#f7f5f5',  	         	  
    #        WHITE, '#f6f5f5', '#efeaea', '#e9dfdd', '#e4d4d0', '#e1c9c1',
    #        '#dfbfb0', '#deb69f', '#deae8c', '#e0a978', '#e2a563', '#e7a54c',  	         	  
    #        '#eca834', '#f3ae1b', TANGERINE, '#f3ae1b', '#eca834', '#e7a54c',  	         	  
    #        '#e2a563', '#e0a978', '#deae8c', '#deb69f', '#dfbfb0', '#e1c9c1',  	         	  
    #        '#e4d4d0', '#e9dfdd', '#efeaea', '#f6f5f5', WHITE, '#f6f6f5',  	         	  
    #        '#efefea', '#e5e9de', '#d5e3d1', '#c3dfca', '#b4ddd1', '#a3d2db',  	         	  
    #        '#91adda', '#857fdb', '#a66bdc', '#dc56df', '#e33f9d', WHITE,  	         	  
    #        '#f6f5f4', '#eeeee8', '#e2e7db', '#cedead', '#beefcc', '#abdbd9',  	         	  
    #        '#99beda', '#858cda', '#9c70dc', '#d159de', '#e341a4',  	         	  
    #        GRAPEFRUIT_PINK, ]  	         	  

    # This color palette contains 100 color steps.  	         	  
    palette = [  	         	  
    '#89ff00', '#a4f817', '#baf12e', '#ccec43', '#d9e758', '#e3e46b', '#e1d97e',  	         	  
    '#e0d18f', '#dfce9f', '#e0ceaf', '#e1d1bd', '#e4d6cb', '#e7ddd7', '#ece5e3',  	         	  
    '#f1eeed', '#f8f7f7', WHITE, '#f8f7f7', '#f1eeed', '#ece4e3', '#e7dbd7',  	         	  
    '#e4d3cb', '#e1cbbd', '#e0c4af', '#dfbf9f', '#e0bd8f', '#e1bc7e', '#e4bf6b',  	         	  
    '#e7c458', '#eccd43', '#f1da2e', '#f8eb17', LEMON, '#f8eb17', '#f1da2e',  	         	  
    '#eccd43', '#e7c458', '#e4bf6b', '#e1bc7e', '#e0bd8f', '#dfbf9f', '#e0c4af',  	         	  
    '#e1cbbd', '#e4d3cb', '#e7dbd7', '#ece4e3', '#f1eeed', '#f8f7f7', WHITE,  	         	  
    '#f7f6f6', '#f1eded', '#ebe4e2', '#e6dad7', '#e3d0ca', '#e0c6bd', '#debeae',  	         	  
    '#deb69f', '#deaf8e', '#dfaa7d', '#e1a66b', '#e4a557', '#e9a643', '#eea92e',  	         	  
    '#f4af17', TANGERINE, '#f4af17', '#eea92e', '#e9a643', '#e4a557', '#e1a66b',  	         	  
    '#dfaa7d', '#deaf8e', '#deb69f', '#debeae', '#e0c6bd', '#e3d0ca', '#e6dad7',  	         	  
    '#ebe4e2', '#f1eded', '#f7f6f6', WHITE, '#f8f7f7', '#f2f1ef', '#ebece5',  	         	  
    '#e2e7db', '#d3e3d0', '#c5e0ca', '#b9ddce', '#abdbd9', '#9ec8da', '#8fa7da',  	         	  
    '#8480db', '#9c70dc', '#c25fde', '#e04dcb', '#e43b8d', WHITE, '#f7f6f6',  	         	  
    '#f0efec', '#e8eae1', '#dae5d5', '#c8e1cb', '#badecd', '#abdbd9', '#9cc4da',  	         	  
    '#8b9cda', '#8d79db', '#b066dd', '#e052da', '#e33e97', GRAPEFRUIT_PINK, ]
    ```
    * How the code smell was fixed:
    ```python
    # This color palette contains 111 color steps.
    palette = [
    '#89ff00', '#a4f817', '#baf12e', '#ccec43', '#d9e758', '#e3e46b', '#e1d97e',
    '#e0d18f', '#dfce9f', '#e0ceaf', '#e1d1bd', '#e4d6cb', '#e7ddd7', '#ece5e3',
    '#f1eeed', '#f8f7f7', '#ffffff', '#f8f7f7', '#f1eeed', '#ece4e3', '#e7dbd7',
    '#e4d3cb', '#e1cbbd', '#e0c4af', '#dfbf9f', '#e0bd8f', '#e1bc7e', '#e4bf6b',
    '#e7c458', '#eccd43', '#f1da2e', '#f8eb17', '#fdff00', '#f8eb17', '#f1da2e',
    '#eccd43', '#e7c458', '#e4bf6b', '#e1bc7e', '#e0bd8f', '#dfbf9f', '#e0c4af',
    '#e1cbbd', '#e4d3cb', '#e7dbd7', '#ece4e3', '#f1eeed', '#f8f7f7', '#ffffff',
    '#f7f6f6', '#f1eded', '#ebe4e2', '#e6dad7', '#e3d0ca', '#e0c6bd', '#debeae',
    '#deb69f', '#deaf8e', '#dfaa7d', '#e1a66b', '#e4a557', '#e9a643', '#eea92e',
    '#f4af17', '#f7b604', '#f4af17', '#eea92e', '#e9a643', '#e4a557', '#e1a66b',
    '#dfaa7d', '#deaf8e', '#deb69f', '#debeae', '#e0c6bd', '#e3d0ca', '#e6dad7',
    '#ebe4e2', '#f1eded', '#f7f6f6', '#ffffff', '#f8f7f7', '#f2f1ef', '#ebece5',
    '#e2e7db', '#d3e3d0', '#c5e0ca', '#b9ddce', '#abdbd9', '#9ec8da', '#8fa7da',
    '#8480db', '#9c70dc', '#c25fde', '#e04dcb', '#e43b8d', '#ffffff', '#f7f6f6',
    '#f0efec', '#e8eae1', '#dae5d5', '#c8e1cb', '#badecd', '#abdbd9', '#9cc4da',
    '#8b9cda', '#8d79db', '#b066dd', '#e052da', '#e33e97', '#e8283f']
    ```
    * [Explain what you changed] It makes more sense to me to have every color written in RGB rather than some with word values. Maybe if every color was named it would be okay.


19. `src/mbrot_fractal.py`, [lines 63, 83-89]
    * [What kind of code smell is this?] Global variable
    * [Why is the smell a problem?] There is no need to make it global. Global variables are harder to incorporate into classes and methods. The variable I'm changing is only used in one method also.
    * Code Snippet:
    ```python
    TWO = 2  # The most important value when determining pixel color

    mainWindowObject = None


    def getPixelColor(c, palette):
        """Return corresponding color from palette depending on iterations to get to TWO"""

        z = complex(0, 0)  # z0
        max_iterations = len(palette)  # only as many iterations as colors in the palette

        for iter in range(max_iterations):
            z = z * z + c  # Get z1, z2, ...  	         	  
            global TWO  	         	  
            if abs(z) > TWO:  	         	  
                z = float(TWO)  	         	  
                return palette[iter]  # provide correct color from color palette
            elif abs(z) < TWO:  	         	  
                continue  	         	  

        # if all iterations complete before reaching 2, return last color in palette
        return palette[-1]
    ```
    * How the code smell was fixed:
    ```python
    mainWindowObject = None

    def getPixelColor(c, palette):
        """Return corresponding color from palette depending on iterations to get to TWO"""

        TWO = 2  # most important value when determining pixel color
        z = complex(0, 0)  # z0
        max_iterations = len(palette)  # only as many iterations as colors in the palette

        for iter in range(max_iterations):
            z = z * z + c  # Get z1, z2, ...  	         	  
            if abs(z) > TWO:  	         	  
                z = float(TWO)  	         	  
                return palette[iter]  # provide correct color from color palette
            elif abs(z) < TWO:  	         	  
                continue  	         	  

        # if all iterations complete before reaching 2, return last color in palette
        return palette[-1]
    ```
    * [Explain what you changed] I shifted the TWO variable into the getPixelColor method so it wouldn't be global anymore. I could just leave it as an integer but I want the reader to know that 2 is a very important number.


20. `src/julia_fractal.py`, [lines 33-55]
    * [What kind of code smell is this?] Naming conventions, dead code, global variables
    * [Why is the smell a problem?] The function name doesn't match that of mbrot_fractal. Dead code takes up space and time. Global variables can be transferred into paramters which makes them more versatile.
    * Code Snippet:
    ```python
    def getColorFromPalette(z):  	         	  
        """Return the index of the color of the current pixel within the Julia set  	         	  
        in the palette array"""  	         	  

        # c is the Julia Constant; varying this value can yield interesting images  	         	  
        c = complex(-1.0, 0.0)  	         	  

        # I feel bad about all of the global variables I'm using.  	         	  
        # There must be a better way...  	         	  
        global grad  	         	  
        global win  	         	  

        # Here 76 refers to the number of colors in the palette  	         	  
        for i in range(78):  	         	  
            z = z * z + c  # Iteratively compute z1, z2, z3 ...  	         	  
            if abs(z) > 2:  	         	  
                return grad[i]  # The sequence is unbounded  	         	  
                z += z + c  	         	  
        # TODO: One of these return statements makes the program crash sometimes  	         	  
        return grad[77]         # Else this is a bounded sequence  	         	  
        return grad[78]
    ```
    * How the code smell was fixed:
    ```python
    def getPixelColor(z, palette):  	         	  
        """Return the color of the current pixel within the Julia set  	         	  
        in the palette array"""  	         	  

        c = complex(-1.0, 0.0)	         	  	         	  
 	         	  
        for color in palette:  	         	  
            z = z * z + c  # Iteratively compute z1, z2, z3 ...  	         	  
            if abs(z) > 2:  	         	  
                return color        	  
        # 
        return palette[-1]
    ```
    * [Explain what you changed] I changed the name of the function to getPixelColor which is the same as the similar function in mbrot_fractal. Then I transferred grad into the palette parameter so I can pass in the list. Then I got rid of code that would never be reached because it's after a return statement. I changed the last return statement to take the last color in the palette list. This will change the color scheme but not the shape. This is because the length of the palette is greater than 78. It's 96. The global win variable never gets used, so I took it out. I added a variable to count the number of times the code would run. I'll also make sure to update where the function is used with the new parameters.


21. `src/julia_fractal.py`, [lines 48-62]
    * [What kind of code smell is this?] Redundancy
    * [Why is the smell a problem?] It's useless code when there's another place that does the same exact thing.
    * Code Snippet:
    ```python
    def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):  	         	  
        """Make sure that the fractal configuration data repository dictionary  	         	  
        contains a key by the name of 'name'  	         	  

        When the key 'name' is present in the fractal configuration data repository  	         	  
        dictionary, return its value.  	         	  

        Return False otherwise  	         	  
        """  	         	  
        for key in dictionary:  	         	  
            if key in dictionary:  	         	  
                if key == name:  	         	  
                    value = dictionary[key]  	         	  
                    return key  
    ```
    * How the code smell was fixed:
    ```python
    # delete section
    ```
    * [Explain what you changed] This function simply checks if the inputted shape name is one of the options for julia_fractal, but main.py already does this for me, so I just took out the whole function.

22. `src/julia_fractal.py`, [lines 69]
    * [What kind of code smell is this?] Bad variable names
    * [Why is the smell a problem?] There are so many parameters, and a lot of them don't get used. Also, one-letter variable names are not descriptive enough.
    * Code Snippet:
    ```python
    def makePictureOfFractal(img, i, e, w, g, p, W, s):
    ```
    * How the code smell was fixed:
    ```python
    def makeFractal(fractal, window, photoImage, bg_color, imageSize):
    ```
    * [Explain what you changed] I got rid of i, e, and g because those parameters were never used. W became bg_color because it's only used once for the background color of the image. I changed w to window because it's only used once to update the window. p became photoImage because it represent the tkinter photo image object. s became size because it is passed in as 512, which is the desired size of the image. img became fractal because it is the name of the fractal shape that will use the "shapes" dictionary.


23. `src/julia_fractal.py`, [lines 67]
    * [What kind of code smell is this?] Global variable
    * [Why is the smell a problem?] There's an unnecessary global variable that only gets called once in main.
    * Code Snippet:
    ```python
    tkPhotoImage = None
    ```
    * How the code smell was fixed:
    ```python
    # delete this section
    ```
    * [Explain what you changed] I just deleted it's original initialization and I'll get rid of "global tkPhotoImage" in main as well.


24. `src/mbrot_fractal.py`, [lines 81-84]
    * [What kind of code smell is this?] Dead code
    * [Why is the smell a problem?] It's code that never gets used.
    * Code Snippet:
    ```python
    def pixelsWrittenSoFar(rows, cols):  	         	  
        pixels = rows * cols  	         	  
        print(f"{pixels} pixels have been output so far")  	         	  
        return pixels
    ```
    * How the code smell was fixed:
    ```python
    # delete this section
    ```
    * [Explain what you changed] I would delete this to make the code cleaner, because it's not doing anything helpful at the moment.


25. `src/julia_fractal.py`, [lines 160-174]
    * [What kind of code smell is this?] Unnecessary comments
    * [Why is the smell a problem?] The comments repeat the name of the variable
    * Code Snippet:
    ```python
    # This is how you write colors for computers
    WHITE = '#ffffff'  # white
    RED = '#ff0000'  # red
    BLUE = '#00ff00'  # blue
    GREEN = '#0000ff'  # green
    BLACK = '#000000'  # black
    ORANGE = '#ffa50'  # orange
    TOMATO = '#ff6347'  # tomato (a shade of red)
    HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)
    REBECCA_PURPLE = '#663399'  # Rebecca Purple
    LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)
    GREY0 = '#000000'  # gray 0 - basically the same as black
    GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36
    GREY74 = '#bdbdbd'  # gray 74 - almost white
    GRAY99 = '#fcfcfc'  # gray 99 - almost white
    ```
    * How the code smell was fixed:
    ```python
    WHITE = '#ffffff'
    RED = '#ff0000'
    BLUE = '#00ff00'
    GREEN = '#0000ff'
    BLACK = '#000000'
    ORANGE = '#ffa50'
    TOMATO = '#ff6347'
    HOT_PINK = '#ff69b4'
    REBECCA_PURPLE = '#663399'
    LIME_GREEN = '#89ff00'
    GREY0 = '#000000'  # similar to black
    GRAY37 = '#5e5e5e'  # lighter than black
    GREY74 = '#bdbdbd'  # almost white
    GRAY99 = '#fcfcfc'  # almost white
    ```
    * [Explain what you changed] I took out the comments about the colors.


26. `src/mbrot_fractal.py`, [lines 81-84]
    * [What kind of code smell is this?] Dead code. Lying comments.
    * [Why is the smell a problem?] It's code that never gets used. The comment says the image is 640x640 instead of 512x512.
    * Code Snippet:
    ```python
    def paint(fractals, imagename, img):
        """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
        This code creates an image which is 640x640 pixels in size."""

        global palette

        fractal = fractals[imagename]
    ```
    * How the code smell was fixed:
    ```python
    def paint(fractal, img, palette):
        """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
        This code creates an image which is 512x512 pixels in size."""
    ```
    * [Explain what you changed] I set up so that the specific would be passed in as the parameter instead of picking the right fractal after the fact. I also turned the global palette into a parameter as well.


27. `src/julia_fractal.py`, [line 177]
    * [What kind of code smell is this?] Bad naming conventions
    * [Why is the smell a problem?] It's hard to understand where the info is coming from if it's named badly.
    * Code Snippet:
    ```python
    def main(i):
    ```
    * How the code smell was fixed:
    ```python
    def main(imageArg):
    ```
    * [Explain what you changed] I'm describing the variable better by naming the parameter imageArg that we get from the user instead of i.

28. `src/mbrot_fractal.py`, [line 126]
    * [What kind of code smell is this?] Bad naming conventions
    * [Why is the smell a problem?] It's hard to understand where the info is coming from if it's named badly.
    * Code Snippet:
    ```python
    def main(image):
    ```
    * How the code smell was fixed:
    ```python
    def main(imageArg):
    ```
    * [Explain what you changed] I'm describing the variable better by naming the parameter imageArg that we get from the user instead of image. The arg part makes it more obvious that it comes from the command line.


29. `src/julia_fractal.py`, [line 126]
    * [What kind of code smell is this?] Naming conventions, distracting comments
    * [Why is the smell a problem?] It's hard to read the code when it has too many comments and badly named variables.
    * Code Snippet:
    ```python
    # Note the time of when we started so we can measure performance improvements
    b4 = time()
    # Set up the GUI so that we can display the fractal image on the screen
    win = Tk()

    # the size of the image we will create is 512x512 pixels
    s = 512
    # construct a new TK PhotoImage object that is 512 pixels square...
    tkPhotoImage = PhotoImage(width=512, height=512)
    # ... and use it to make a picture of a fractal
    makeFractal(shapes[imageArg], win, tkPhotoImage, GREY0, 512)

    # Write out the Fractal into a .gif image file  	         	  
    tkPhotoImage.write(imageArg + ".png")
    print(f"Done in {time() - b4:.3f} seconds!", file=sys.stderr)  	         	  

    # Output the Fractal into a .png image  	         	  
    tkPhotoImage.write(imageArg + ".png")
    print("Wrote picture " + imageArg + ".png")
    tkPhotoImage.write(imageArg + ".png")

    # print a message telling the user how to quit or exit the program  	         	  
    print("Close the image window to exit the program")  	         	  
    # Call tkinter.mainloop so the GUI remains open  	         	  
    mainloop()
    ```
    * How the code smell was fixed:
    ```python
    before = time()
    win = Tk()
    img = PhotoImage(width=512, height=512)
    makeFractal(shapes[imageArg], win, img, GREY0, 512)
    
    # save the image as a PNG file
    img.write(imageArg + ".png")
    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)  	         	  
    img.write(imageArg + ".png")
    print("Wrote picture " + imageArg + ".png")

    # Call tkinter.mainloop so the GUI remains open  	         	  
    print("Close the image window to exit the program")  	         	  
    mainloop()
    ```
    * [Explain what you changed] I removed a lot of the comments that were distracting from actual code. I also renamed the b4 variable to before for clarity and made an after variable to specify that we're trying to find the difference between them to calculate the runtime of the program.


30. `src/julia_fractal.py`, [lines 77-106, 137]
    * [What kind of code smell is this?] Redundancy
    * [Why is the smell a problem?] I don't think it's necessary to repack the canvas multiple times in a row. I'm also going to take out some comments so the code is cleaner.
    * Code Snippet:
    ```python
    # Display the image on the screen
    canvas = Canvas(win, width=imageSize, height=imageSize, bg=bg_color)

    # pack the canvas object into its parent widget
    canvas.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?

    # Create the TK PhotoImage object that backs the Canvas Objcet
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals
    canvas.create_image((imageSize/2, imageSize/2), image=photoImage, state="normal")
    canvas.pack()  # This seems repetitive
    canvas.pack()  # But it is how Larry wrote it the tutorial
    canvas.pack()  # Larry's a smart guy.  I'm sure he has his reasons.

    # Total number of pixels in the image, AKA the area of the image, in pixels
    area_in_pixels = 640 * 640

    # pack the canvas object into its parent widget
    canvas.pack()  # Does this even matter?
    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
    size = abs(maxx - minx) / imageSize

    # pack the canvas object into its parent widget
    canvas.pack()

    # Keep track of the fraction of pixels that have been written up to this point in the program
    fraction_of_pixels_writtenSoFar = int(imageSize / 64)
    
    #...
    
    fraction_of_pixels_writtenSoFar += 640  # update the number of pixels output so far
    ```
    * How the code smell was fixed:
    ```python
    # Display the image on the screen
    canvas = Canvas(win, width=imageSize, height=imageSize, bg=bg_color)
    canvas.pack()
    canvas.create_image((imageSize/2, imageSize/2), image=photoImage, state="normal")
    
    size = abs(maxx - minx) / imageSize
    ```
    * [Explain what you changed] I got rid of all of the repeat pack commands, because I don't think they matter. I'm not sure so I'll have to test it but it should work alright. I also took out the fraction_of_pixels_writtenSoFar because it's only used when it counts up but is useless still. I also took out comments for readability purposes. I might add some back in but what was there was overkill.


31. `src/julia_fractal.py`, [line 126]
    * [What kind of code smell is this?] Readability, naming conventions
    * [Why is the smell a problem?] It's impossible to tell what's going on. I also just want to try and see if the comments are lying and I can do a forwards for loop.
    * Code Snippet:
    ```python
    # for r (where r means "row") in the range of the size of the square image,
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to
    # but I have to here because we're actually going BACKWARDS, which took me
    # a long time to figure out, so don't change it, or else the picture won't
    # come out right
    for r in range(imageSize, 0, -1):
        # for c (c == column) in the range of pixels in a square of size s
        for c in range(imageSize):
            # calculate the X value in the complex plane (I guess that's
            # actually the REAL number part, but we call it X because
            # GRAPHICS... whatev)
            x = minx + c * size
            y = 0
            # get the color of the pixel at this point in the complex plain
            c2 = getPixelColor(complex(x, y), palette)
            # calculate the X value in the complex plane (but I know this is
            # really the IMAGINARY axis that we're talking about here...)
            y = miny + r * size
            # TODO: do I really need to call getPixelColor() more than o, palettence?
            #       It feels like that might be kinda slow...
            #       But, if it aint broken, don't repair it, right?
            # get the color of the pixel at this point in the complex plain
            c2 = getPixelColor(complex(x, y), palette)
            # put the color c2 into the
            photoImage.put(c2, (c, imageSize - r))
            # get the color of the pixel at this point in the complex plain
            c2 = getPixelColor(complex(x, y), palette)  # does it matter if
        window.update()  # display a row of pixels
    ```
    * How the code smell was fixed:
    ```python
    for row in range(imageSize, 0, -1):
        # for c (c == column) in the range of pixels in a square of size s
        for col in range(imageSize):
            x = minx + col * size
            y = 0
            # get the color of the pixel at this point in the complex plain
            # c2 = getPixelColor(complex(x, y), palette)
            y = miny + row * size
            # get the color of the pixel at this point in the complex plain
            c2 = getPixelColor(complex(x, y), palette)
            photoImage.put(c2, (col, imageSize - row))
            # get the color of the pixel at this point in the complex plain
            # c2 = getPixelColor(complex(x, y), palette)  # does it matter if
        window.update()  # display a row of pixels
    ```
    * [Explain what you changed] I looked at where c2 is actually used, and I only updated it right before that. I also removed most of the comments. There's also no need to declare y twice.
