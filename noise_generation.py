import numpy as np
import wave
import random
import scipy.io.wavfile

from os import path

def combine_audio_files(files, output_file):
    combined_signal = None
    sample_rate = None

    # Iterate over each file
    for file in files:
        # Read the audio file
        sample_rate, audio_data = scipy.io.wavfile.read(file)

        # Initialize combined signal if not yet initialized
        if combined_signal is None:
            combined_signal = audio_data
        else:
            # Make sure all signals have the same length
            min_length = min(len(combined_signal), len(audio_data))
            combined_signal = combined_signal[:min_length]
            audio_data = audio_data[:min_length]

            # Combine the signals
            combined_signal += audio_data

    # Save the combined audio to a new file
    if combined_signal is not None and sample_rate is not None:
        scipy.io.wavfile.write(output_file, sample_rate, combined_signal)
    else:
        print("error")

def combine(files, output_file):
    combined = []

    sample_rate = 10000
    for file in files:
        sample_rate, data = scipy.io.wavfile.read(file)
        data = data.astype(np.float32) / 32767.0
        combined.append(data)

    combined = np.sum(combined, axis=0)

    combined = np.int16(combined / np.max(np.abs(combined)) * 32767)

    scipy.io.wavfile.write(output_file, sample_rate, combined)

def create_propeller_noise(filename, sample_rate=44100, max_frequencies=10):
    if path.isfile(filename):
        return

    frequencies = [random.randint(20, 250) for _ in range(random.randint(1, max_frequencies))]
    print(f"Propeller frequenices: {frequencies}")

    x = np.linspace(0, 1, sample_rate)  # the points on the x axis for plotting

    # compute the value (amplitude) of the sin wave for each sample
    random_waves = []
    for f in frequencies:
        random_waves.append(np.sin(2 * np.pi * f * x))

    # Adds the sine waves together into a single complex wave
    combined_wave = np.sum(random_waves, axis=0)
    scaled_wave = np.int16(combined_wave / np.max(np.abs(combined_wave)) * 32767)

    # Open a new WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(scaled_wave.tobytes())

def create_random_noise(filename, sample_rate=44100, max_frequesncies=100):

    frequencies = [random.randint(20, 2000) for _ in range(random.randint(1, max_frequesncies))]
    print(f"Random frequencies: {frequencies}")
    x = np.linspace(0, 1, sample_rate)  # the points on the x axis for plotting

    # compute the value (amplitude) of the sin wave for each sample
    random_waves = []
    for f in frequencies:
        random_waves.append(np.sin(2 * np.pi * f * x))

    # Adds the sine waves together into a single complex wave
    combined_wave = np.sum(random_waves, axis=0)
    scaled_wave = np.int16(combined_wave / np.max(np.abs(combined_wave)) * 32767)

    # Open a new WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(scaled_wave.tobytes())
    

def create_noise(output_file, sample_rate):
    create_propeller_noise("sample_audio/propeller_noise.wav", sample_rate, max_frequencies=1)
    
    create_random_noise("sample_audio/random_noise.wav", sample_rate, max_frequesncies=1)
    
    combine(["sample_audio/random_noise.wav", "sample_audio/propeller_noise.wav"], output_file)

def simulate_noise(noise_samples=5, sample_rate=44100):
    for i in range(noise_samples):
        file_name = "sample_audio/sample_" + str(i)  + ".wav"
        create_noise(file_name, sample_rate)

import matplotlib.pyplot as plt

from wav.plot import plot_single_file

simulate_noise(noise_samples=1, sample_rate=44100)

plot_single_file("sample_audio/sample_0.wav")
plt.show()