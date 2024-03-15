# import librosa
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile

def get_fourier_frequencies(file):
    # Read the audio file
    sample_rate, data = scipy.io.wavfile.read(file)

    # Compute the Fourier Transform
    fourier = np.fft.fft(data)
    fourier = np.abs(fourier)
    print(fourier)    

    # Compute the frequencies
    n = len(fourier)
    freq = np.fft.fftfreq(n, d=1/sample_rate)
    print(freq.sort)

    _, c1 = plt.subplots()
    c1.plot(fourier, color="green")
    plt.show()

    return freq, fourier

freq, fourier = get_fourier_frequencies("sample_audio/sample_0.wav")

# def get_fourier_frequencies(wav_file):
#     # Open the audio file
#     with wave.open(wav_file, 'rb') as wf:
#         # Read the audio data
#         data = wf.readframes(-1)
#         data = np.frombuffer(data, dtype=np.int16)

#         # Get the sample rate
#         sample_rate = wf.getframerate()

#         # Get the frequencies
#         fft = np.fft.rfft(data)
#         fft = np.abs(fft)
#         return fft, sample_rate
        