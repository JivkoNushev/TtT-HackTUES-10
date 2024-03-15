import numpy as np
import matplotlib.pyplot as plt
import random

#Get plots
fig, c1 = plt.subplots()
c2 = c1.twinx()

fs = 100 # sample rate 
f_list = [5,10,15,20,100] # the frequency of the signal
# f_list = [20, 40] # the frequency of the signal

x = np.arange(fs) # the points on the x axis for plotting
print((x/fs))

# compute the value (amplitude) of the sin wave for each sample
wave = []
for f in f_list:
    wave.append(list(np.sin(2*np.pi*f * (x/fs))))

# #Plot the sine waves
# c1.plot(wave[0], color="blue")
# c1.plot(wave[1], color="yellow")

#Adds the sine waves together into a single complex wave
wave4 = []
for i in range(len(wave[0])):
    data = 0
    for ii in range(len(wave)):
        data += wave[ii][i]
    wave4.append(data)

#Get frequencies from complex wave
fft = np.fft.rfft(wave4)
fft = np.abs(fft)

#Note: Here I will add some code to remove specific frequencies

#Get complex wave from frequencies
waveV2 = np.fft.irfft(fft)

#Plot the complex waves, should be the same
c1.plot(wave4, color="orange")
# c1.plot(waveV2)

# c1.plot(fft, color="green")
plt.show()