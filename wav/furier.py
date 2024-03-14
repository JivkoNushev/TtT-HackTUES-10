import scipy.io.wavfile
import numpy as np

# Load the two audio files
sample_rate_output, output = scipy.io.wavfile.read('sample_audio/output.wav')
