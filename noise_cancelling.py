import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# generate noise
# from noise_generation import simulate_noise
# simulate_noise(noise_samples=5, sample_rate=1000)

from fourier import plot_file_fourier, get_fourier_frequencies

common_freqs = {}

def add_sample(filename):
    freqs, dict_, fourier = get_fourier_frequencies(filename)

    for i in range(len(freqs)):
        if (freqs[i], dict_["peak_heights"][i]) in common_freqs:
            common_freqs[(freqs[i], dict_["peak_heights"][i])] += 1
        else:
            common_freqs[(freqs[i], dict_["peak_heights"][i])] = 1

def get_common_freqs(files):
    for file in files:
        add_sample(file)

    max_count = max(common_freqs.values())
    return [key for key, value in common_freqs.items() if value == max_count]

def get_propeller_noise(files):
    most_common_freqs = get_common_freqs(files)
    fs = 1000  # sample rate 

    x = np.linspace(0, 1, fs)  # the points on the x axis for plotting
    propeller_noise = 0
    # print(most_common_freqs)
    for (frequency, amplitude) in most_common_freqs:
        propeller_noise = amplitude * np.sin(2*np.pi*frequency*x)

    # fr36 = 250 * np.sin(2*np.pi*40*x)

    propeller_noise = -propeller_noise

    return propeller_noise

def demo():

    # get random noise from first file
    _, sample_0_noise = wav.read("sample_audio/sample_0.wav")
    sample_0_noise = sample_0_noise.astype(np.float32) / 32767.0
    _, c1 = plt.subplots()
    c1.plot(sample_0_noise, color="blue")

    # fourier on file
    plot_file_fourier("sample_audio/sample_0.wav")

    # get reverse propeller noise from fourier 
    reversed_propeller_noise = get_propeller_noise(["sample_audio/sample_0.wav", "sample_audio/sample_1.wav", "sample_audio/sample_2.wav", "sample_audio/sample_3.wav", "sample_audio/sample_4.wav"])
    
    _, c1 = plt.subplots()
    c1.plot(reversed_propeller_noise, color="orange")

    # apply the reverse propeller noise to the first file sample
    _, c1 = plt.subplots()
    c1.plot(sample_0_noise - reversed_propeller_noise, color="purple")
    
    # show plots of the different steps
    plt.show()

# demo
demo()