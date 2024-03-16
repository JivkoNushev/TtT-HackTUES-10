import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.io.wavfile as wav

# Get plots
fig, c1 = plt.subplots()
c2 = c1.twinx()
fig, c2 = plt.subplots()

fs = 10000  # sample rate 
f_list = [23, 60]  # the frequency of the signal

x = np.linspace(0, 1, fs)  # the points on the x axis for plotting

# Compute the value (amplitude) of the sin wave for each sample
wave = []
for f in f_list:
    wave.append(np.sin(2 * np.pi * f * x))

# c2.plot(wave[2], color="blue")

# Adds the sine waves together into a single complex wave
wave4 = np.sum(wave, axis=0)
from wav.plot import plot_single_file

_, data = wav.read("sample_audio/sample_0.wav")
fig, c4 = plt.subplots()
c4.plot(data, color="blue")

scaled_wave = np.int16(wave4 / np.max(np.abs(wave4)) * 32767)
c2.plot(scaled_wave, color="green")

import wave as wv

# Open a new WAV file
with wv.open("b.wav", 'wb') as wf:
    wf.setnchannels(1)  # Mono
    wf.setsampwidth(2)  # 16-bit
    wf.setframerate(10000)
    wf.writeframes(scaled_wave.tobytes())

new_scaled_w = 0
with wv.open("b.wav", 'rb') as wf:
    # Read the audio data
    data = wf.readframes(-1)
    data = np.frombuffer(data, dtype=np.int16)
    data = data.astype(np.float32) / 32767.0

    # Get the sample rate
    sample_rate = wf.getframerate()
    new_scaled_w = data

# Get frequencies from complex wave
fft = np.fft.rfft(new_scaled_w)
fft = np.abs(fft)

# Get the corresponding frequencies for the FFT
frequencies = np.fft.rfftfreq(len(new_scaled_w), d=1/fs)

peaks, _ = signal.find_peaks(fft, height=1)
print(peaks)

# Plot the frequency spectrum
c1.plot(frequencies, fft, color="green")
c1.set_xlim(0, 20000)  # Set x-axis limit to 0-20 kHz
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
plt.grid()
plt.show()