#import fah_converter
#import fah_converter as fah
#from fah_converter import convert_c_to_f
from fah_converter import *

print("Enter a celsius value: ")
celsius = float(input())
#fahrenheit = fah_converter.convert_c_to_f(celsius)
#fahrenheit = fah.convert_c_to_f(celsius)
fahrenheit = convert_c_to_f(celsius)
print("That's ", fahrenheit, " degrees Fahrenheit")