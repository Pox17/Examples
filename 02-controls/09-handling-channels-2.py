from pyo import *

# Creates a Server with 8 channels
s = Server(nchnls=8).boot()

# Generates a sine wave
a = Sine(freq=500, mul=0.3)

# Mixes it up to four streams
b = a.mix(4)

# Outputs to channels 0, 2, 4 and 6
b.out(chnl=0, inc=2)

s.gui(locals())