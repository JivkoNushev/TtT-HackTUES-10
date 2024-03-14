import matplotlib.pyplot as plt
import scipy.io.wavfile
import numpy as np

# https://stackoverflow.com/questions/64410196/how-to-plot-a-waveform-from-wav-file-in-python

myAudioFilename = 'sample_audio/water.wav'
sampleRate, audioBuffer = scipy.io.wavfile.read(myAudioFilename)

duration = len(audioBuffer)/sampleRate
time = np.arange(0,duration,1/sampleRate)

plt.plot(time,audioBuffer)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title(myAudioFilename)
plt.show()