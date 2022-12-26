# Fractal Visualizer User Manual

* You will be accessing the fractal-making program through the command line.
* This means you'll be running `$ python src/main.py` when in the cs1440-hassett-ally-assn4 directory.
* There are also two additional (optional) arguments to add when you run the program.
  * You can choose the fractal that will be drawn by adding the name of the file. It will probably be a `.frac` file but it doesn't have to be. It's just less likely to have the necessary data in the proper format.
    * It's good to check the `data/` subdirectory for a `.frac` file. There's lots of options in there and most won't crash the program.
    * If you choose a non-existent file for this argument, the program will crash. You have been warned.
    * If you choose a file that's not formatted properly with the correct data, the program will raise an error. Note that the program will only raise the first error it reaches.
  * You can also choose the color scheme of the image produced. My two options are `Mismatch` and `Complementary`. (Capitalization does not matter.) You'll put one of those two names as your second optional argument.
    * If you put a random color scheme there besides one of these two, the program will give you an error and then crash.
* If you choose not to add these optional arguments, the program will run the default which I have set to be a seahorse shape for the fractal and Complementary for the palette.
* If you choose to only add one of the optional arguments, it must be the name of the file you wish to read the fractal data from. This is what the program will assume is in that argument spot. If you put a color scheme with no file, the program will crash.