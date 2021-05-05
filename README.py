# colored-text-changer
# This is a simple program that changes the color of the text

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.ORANGE+Back.BLACK+"Welcome to this new app. " + Fore.GREEN+Back.White + "You can now set your settings.")
print(Fore.RED+"You can now customize your app any how you want too.")
print(Back.GREEN + Back.WHITE"Your username can be whatever you want it to be.")
print(Fore.BROWN + "How many licks does it take to get to the center of a tootsie pop?")
