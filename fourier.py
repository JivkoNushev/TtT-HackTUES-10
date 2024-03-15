import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import wave
import scipy.signal as signal


def read_wav(wav_file):
    with wave.open(wav_file, 'rb') as wf:
        # Read the audio data
        data = wf.readframes(-1)
        data = np.frombuffer(data, dtype=np.int16)
        data = data.astype(np.float32) / 32767.0

        # Get the sample rate
        sample_rate = wf.getframerate()
        print (sample_rate)
        return sample_rate, data

def get_fourier_frequencies(wav_file):
    # Open the audio file
    _, data = read_wav(wav_file)
    
    # _, c3 = plt.subplots()
    # c3.plot(data, color="blue")

    # Get the frequencies
    fourier = np.fft.rfft(data)
    fourier = np.abs(fourier)

    # Get the corresponding frequencies for the FFT
    # frequencies = np.fft.rfftfreq(len(data), d=1/sample_rate)
    peaks, _ = signal.find_peaks(fourier, height=1)

    # # Plot the frequency spectrum
    # _, c1 = plt.subplots()
    # c1.plot(frequencies, fourier, color="green")
    # c1.set_xlim(0, 20000)  # Set x-axis limit to 0-20 kHz
    # plt.xlabel('Frequency (Hz)')
    # plt.ylabel('Amplitude')
    # plt.title('Frequency Spectrum')
    # plt.grid()

    return peaks, fourier

# peaks = get_fourier_frequencies("sample_audio/sample_0.wav")
# print(peaks)

