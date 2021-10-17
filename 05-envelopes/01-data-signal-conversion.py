from __future__ import print_function
from pyo import *

s = Server().boot()

# A python integer (or float).
anumber = 100

# Conversion from number to an audio stream (vector of floats).
astream = Sig(anumber)

# Use a Print (capital "P") object to print an audio stream.
pp = Print(astream, interval=0.1, message="Audio stream value")

# Use the get() method to extract a float from an audio stream.
print("Float from audio stream : ", astream.get())

s.gui(locals())