import wave

rand_file = open("/dev/urandom", "rb")

analog_values = []
analog_values_inverted = []


SAMPLE_RATE = 44100
SAMPLE_RATE = 1
SAMPLE_WIDTH = 1 << 16 - 1
SAMPLE_WIDTH_BYTES = 2
NUM_SAMPLES_TO_WRITE = SAMPLE_RATE * 12


for i in range(NUM_SAMPLES_TO_WRITE):
    # value = int.from_bytes(rand_file.read(4), "little") % SAMPLE_WIDTH
    value = (SAMPLE_WIDTH // 2) + i % SAMPLE_WIDTH
    if value != 0:
        original_value = value

        value = original_value - SAMPLE_WIDTH // 2

        analog_values.append(value.to_bytes(2, "little", signed=True))

        value = (-SAMPLE_WIDTH // 2) + (SAMPLE_WIDTH - original_value)

        analog_values_inverted.append(value.to_bytes(2, "little", signed=True))
    else:
        print("Found zero value")


print(analog_values)
print(analog_values_inverted)

wav_file = wave.open("sample_audio/output.wav", "w")
wav_file.setnchannels(1)
wav_file.setsampwidth(SAMPLE_WIDTH_BYTES)
wav_file.setframerate(SAMPLE_RATE)
wav_file.writeframes(b"".join(analog_values))

wav_file = wave.open("sample_audio/output_inverted.wav", "w")
wav_file.setnchannels(1)
wav_file.setsampwidth(SAMPLE_WIDTH_BYTES)
wav_file.setframerate(SAMPLE_RATE)
wav_file.writeframes(b"".join(analog_values_inverted))
