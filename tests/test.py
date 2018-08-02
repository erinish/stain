#!/usr/bin/python3
from stain import Stain

stain = Stain(True)

with stain.red():
    print("test")

with stain.blue():
    print("test")

with stain.green():
    print("test")

with stain.green_on_black():
    print("test" + stain.RESET)

with stain.underline_blue():
    print("muahahaha", end='')
print(" - some normal text")


def print_error(msg):
    with stain.red_on_black():
        print('ERROR:', end='')
    print(" " + msg)

print_error('something went horribly wrong.')

print(stain.RED + 'RED:' + stain.WHITE + 'WHITE:' + stain.BLUE + 'BLUE' + stain.RESET)

with stain.black_on_light_gray():
    print("This will have a background color" + stain.RESET)

print(stain.BOLD_RED_ON_BLACK_UNDERLINE + "MY EYES" + stain.RESET)

print("Hello " + stain.BLACK + " darkness " + stain.RESET + "my old friend.")
