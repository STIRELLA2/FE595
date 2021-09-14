
#FE 595 HW 1: Spencer Tirella

import numpy as np

import matplotlib.pyplot as plot

# X Values
x = np.arange(0, 10, 0.1)

# Y and Z cosine and sine
y = np.sin(x)
z = np.cos(x)

# Plot
plot.plot(x,y,x,z)

# Title and axis labels
plot.title('Sine and Cosine Wave')
plot.xlabel('Time')
plot.ylabel('Amplitude')

#Plot Colors
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.legend(['sin(x)', 'cos(x)'])
plot.show()