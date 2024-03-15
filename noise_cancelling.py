import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from fourier import get_fourier_frequencies
from wav.plot import plot_single_file

def get_propeller_noise():
    fs = 1000  # sample rate 

    # plot_single_file("sample_audio/sample_0.wav")

    # read the audio data
    


    freqs, dict_, fourier = get_fourier_frequencies("sample_audio/sample_0.wav")

    for i in range(len(fourier)):
        if i not in freqs:
            fourier[i] = 0

    rev_f = np.fft.irfft(fourier)

    frequencies = np.fft.rfftfreq(len(fourier), d=1/fs)
    print(dict_)

    _, original = wav.read("sample_audio/sample_0.wav")
    original = original.astype(np.float32) / 32767.0

    _, c1 = plt.subplots()
    c1.plot(fourier, color="green")

    _, c1 = plt.subplots()
    c1.plot(rev_f, color="red")
    c1.plot(original, color="green")


    # print(freqs)

    # x = np.linspace(0, 1, fs)  # the points on the x axis for plotting
    
    # not_def_wave = []
    # for f in freqs:
    #     not_def_wave.append(np.sin(2 * np.pi * f * x))
    
    # combined_waves = -np.sum(not_def_wave, axis=0)
    # _, c1 = plt.subplots()
    # c1.plot(combined_waves, color="green")

    # _, c1 = plt.subplots()
    # c1.plot(not_def_wave[1], color="green")

    # _, c1 = plt.subplots()
    # c1.plot(combined_waves + original, color="green")

    # print(original)
    # print(combined_waves)

    plt.show()



get_propeller_noise()
