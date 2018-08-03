#!/usr/bin/python3
from stain import Stain

stain = Stain(True)

with stain.red():
    print("red")

with stain.blue():
    print("blue")

with stain.green():
    print("green")

with stain.green_on_black():
    print("green on black background" + stain.RESET)

with stain.underline_blue():
    print("Underlined Text", end='')
print(" - some normal text")


with stain.red_on_black():
    print('ERROR:' + stain.RESET + " something went horribly right.")


print(stain.RED + 'RED:' + stain.WHITE + 'WHITE:' + stain.BLUE + 'BLUE' + stain.RESET)

with stain.black_on_light_gray():
    print("This will have a background color" + stain.RESET)

print(stain.BOLD_RED_ON_BLACK_UNDERLINE + "MY EYES" + stain.RESET)

print("Hello " + stain.BLACK + " darkness " + stain.RESET + "my old friend.")

with stain.on_blue_dim_yellow():
    print("Strange ordering still works" + stain.RESET)

print(stain.YELLOW_BOLD_ON_BLUE_ON_RED_UNDERLINE_ON_BLACK + "exclusive stacking overrides -- this should be bold yellow on black underlined" + stain.RESET)
