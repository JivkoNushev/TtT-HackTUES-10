import scipy.io.wavfile
import numpy as np

def combine_audio_files(files):
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
        scipy.io.wavfile.write('sample_audio/combined.wav', sample_rate, combined_signal)
    else:
        print("error")
# Example usage:
files_to_combine = ['sample_audio/1.wav', 'sample_audio/2.wav', 'sample_audio/main.wav']
combine_audio_files(files_to_combine)
