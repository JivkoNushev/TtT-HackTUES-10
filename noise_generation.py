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

def create_propeller_noise(filename, duration=1.0, sample_rate=44100, max_frequencies=10):
    if path.isfile(filename):
        return

    num_samples = int(duration * sample_rate)

    frequencies = [random.randint(0, 1000) for _ in range(random.randint(0, max_frequencies))]

    x = np.arange(num_samples)  # the points on the x axis for plotting

    # compute the value (amplitude) of the sin wave for each sample
    random_waves = []
    for f in frequencies:
        random_waves.append(np.sin(2 * np.pi * f * (x / sample_rate)))

    # Adds the sine waves together into a single complex wave
    combined_wave = np.sum(random_waves, axis=0)

    # Scale the waveform to fit in the range [-32768, 32767] (16-bit PCM)
    scaled_wave = np.int16(combined_wave * 32767)

    # Open a new WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(scaled_wave.tobytes())

def create_random_noise(filename, duration=1.0, sample_rate=44100, max_frequesncies=100):
    num_samples = int(duration * sample_rate)

    frequencies = [random.randint(20, 20000) for _ in range(random.randint(0, max_frequesncies))]

    x = np.arange(num_samples)  # the points on the x axis for plotting

    # compute the value (amplitude) of the sin wave for each sample
    random_waves = []
    for f in frequencies:
        random_waves.append(np.sin(2 * np.pi * f * (x / sample_rate)))

    # Adds the sine waves together into a single complex wave
    combined_wave = np.sum(random_waves, axis=0)

    # Scale the waveform to fit in the range [-32768, 32767] (16-bit PCM)
    scaled_wave = np.int16(combined_wave * 32767)

    # Open a new WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(scaled_wave.tobytes())
    

def create_noise(output_file, sample_rate=44100):
    create_propeller_noise("sample_audio/propeller_noise.wav", sample_rate)
    create_random_noise("sample_audio/random_noise.wav", sample_rate)

    combine_audio_files(["sample_audio/random_noise.wav", "sample_audio/propeller_noise.wav"], output_file)

def simulate_noise_capture(noise_samples=5, sample_rate=44100):
    for i in range(noise_samples):
        file_name = "sample_audio/sample_" + str(i)  + ".wav"
        create_noise(file_name, sample_rate)

# import matplotlib.pyplot as plt

# from wav.plot import plot_single_file

simulate_noise_capture(sample_rate=1/1000)

# plot_single_file("sample_audio/sample1.wav")
# # plot_single_file("sample_audio/sample2.wav")
# plt.show()