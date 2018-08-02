# Stain 

Taking care of the dirty details of outputting terminal colors.

## Getting Started

Using the basics of stain is fast and easy. 

Out of the box, stain provides a context manager that handles pre-printing of
formatting characters before the block executes and post-printing of a formatting
reset.

Ex:
```PYTHON
from stain import Stain

stain = Stain()

with stain.red():
    print("This line is red.")
    print("So is this one.")

print("But this one is not.")
```

For more complex coloring, stain also provides formatting constants.

```PYTHON
from stain import Stain

stain = Stain()

print("Hello " + stain.BLACK + " darkness " + stain.RESET + "my old friend.")
```


Both forms of stain can take stacked attributes in any order:

```PYTHON
stain.BLACK_ON_RED
```
or
```PYTHON
with stain.bold_green():
```
or even
```PYTHON
stain.BOLD_RED_ON_BLACK_UNDERLINE
```

### Terminal Detection
Stain is TTY-aware, meaning it will not print coloring characters when your output
has been redirected to files, pagers, etc. 


### Supported Formatting

Stain supports 16-Color ANSI foreground and background colors, and the common formatters.

Whether or not a given terminal supports them is another matter. 

COLORS:
* Black
* Red
* Green
* Yellow
* Blue
* Magenta
* Cyan
* Light gray
* Dark gray
* Light red
* Light green
* Light yellow
* Light magenta
* Light cyan
* White

FORMATS:
* Bold
* Reset Bold
* Dim
* Reset Dim
* Underline
* Reset Underline
* Blink
* Reset Blink
* Reverse
* Reset Reverse
* Hidden
* Reset Hidden
* Reset All

#### Caveat Regarding Background Coloring

By default, background coloring is disabled in the context manager form of stain.
This is due to how background color determination works when scrolling a terminal.

When printing a newline at the bottom of the screen such that everything needs to shift
upward, the background color will bleed onto the next line. The context manager cannot
print the reset before print statements in the block print theirs, so ugly background
color bleeding will occur. 

This is also true of the Inverse formatter.

To enable background colors with the context manager, do the following:
```PYTHON
from stain import Stain

stain = Stain(unsafe=True)

with stain.black_on_light_gray():
    print("This will have a background color" + stain.RESET)
```

You will need to hand-reset at the end of each line to prevent scrolling background bleed.


### Prerequisites

 None

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

make tests

## Deployment

Add additional notes about how to deploy this on a live system

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
