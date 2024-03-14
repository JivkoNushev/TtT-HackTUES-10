# https://stackoverflow.com/questions/64410196/how-to-plot-a-waveform-from-wav-file-in-python

import matplotlib.pyplot as plt
import scipy.io.wavfile
import numpy as np

def plot_file(audioFilename):
    sampleRate, audioBuffer = scipy.io.wavfile.read(audioFilename)

    duration = len(audioBuffer) / sampleRate
    time = np.arange(0, duration, 1/sampleRate)

    plt.figure()
    plt.plot(time, audioBuffer)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title(audioFilename)

def plot_files(audioFilenames):
    for audioFilename in audioFilenames:
        sampleRate, audioBuffer = scipy.io.wavfile.read(audioFilename)

        duration = len(audioBuffer) / sampleRate
        time = np.arange(0, duration, 1/sampleRate)

        plt.plot(time, audioBuffer)
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title(audioFilename)

# Plot each file in a separate window
plot_file('sample_audio/output.wav')
plot_file('sample_audio/output_inverted.wav')
plot_file('sample_audio/output_inverted.wav')

plot_files(['sample_audio/output.wav', 'sample_audio/output_inverted.wav'])

plt.show()