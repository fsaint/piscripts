from inky import InkyWHAT
from PIL import Image
import sys

inkywhat = InkyWHAT('red')

#img = Image.open("InkywHAT-400x300.png")
img = Image.open("keystrokes_bw.png")

inkywhat.set_image(img)

inkywhat.show()



