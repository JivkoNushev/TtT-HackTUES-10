import matplotlib.pyplot as plt
import scipy.io.wavfile
import numpy as np

def plot_single_file(audioFilename):
    sampleRate, audioBuffer = scipy.io.wavfile.read(audioFilename)

    duration = len(audioBuffer) / sampleRate
    time = np.arange(0, duration, 1/sampleRate)

    plt.figure()  # Create a new figure for each plot
    plt.plot(time, audioBuffer)
    plt.axhline(0, color='red', linestyle='--')  # Add a line at y=0
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title(audioFilename)

def plot_multiple_files(audioFilenames):
    plt.figure()  # Create a new figure for all plots
    for audioFilename in audioFilenames:
        sampleRate, audioBuffer = scipy.io.wavfile.read(audioFilename)

        duration = len(audioBuffer) / sampleRate
        time = np.arange(0, duration, 1/sampleRate)

        plt.plot(time, audioBuffer, label=audioFilename)

    plt.axhline(0, color='red', linestyle='--')  # Add a line at y=0
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Waveform Comparison')
    plt.legend()

plot_single_file('sample_audio/output.wav')
plot_single_file('sample_audio/output_inverted.wav')
plot_multiple_files(['sample_audio/output.wav', 'sample_audio/output_inverted.wav'])

plt.show()
