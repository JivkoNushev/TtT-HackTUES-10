import scipy.io.wavfile
import numpy as np

# Load the two audio files
sample_rate_output, output = scipy.io.wavfile.read('sample_audio/output.wav')
sample_rate_inverted, inverted = scipy.io.wavfile.read('sample_audio/output_inverted.wav')

# Make sure both audio signals have the same length
min_length = min(len(output), len(inverted))
output = output[:min_length]
inverted = inverted[:min_length]

# Combine the two audio signals
combined = output + inverted

# Save the combined audio to a new file
scipy.io.wavfile.write('sample_audio/combined.wav', sample_rate_output, combined)
