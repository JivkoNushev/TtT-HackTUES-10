import wave

# rand_file = open("/dev/urandom", "rb")

analog_values = []
analog_values_inverted = []


SAMPLE_RATE_IN_HZ = 44100
SAMPLE_WIDTH = 1 << 16 - 1
NUM_SAMPLE_BYTES_TO_WRITE = SAMPLE_RATE_IN_HZ * 10
negative = -1


for i in range(NUM_SAMPLE_BYTES_TO_WRITE):
    # value = int.from_bytes(rand_file.read(4), "little") % SAMPLE_WIDTH
    value = i % SAMPLE_WIDTH
    # if not value:
    #     negative = -negative

    # if negative:
    #     value = -value
    if value > 0:
        analog_values.append(value.to_bytes(2, "little"))
        analog_values_inverted.append((SAMPLE_WIDTH - value).to_bytes(2, "little"))


print(analog_values)
print(analog_values_inverted)

wav_file = wave.open("sample_audio/output.wav", "w")
wav_file.setnchannels(1)
wav_file.setsampwidth(2)
wav_file.setframerate(44100)
wav_file.writeframes(b"".join(analog_values))

wav_file = wave.open("sample_audio/output_inverted.wav", "w")
wav_file.setnchannels(1)
wav_file.setsampwidth(2)
wav_file.setframerate(44100)
wav_file.writeframes(b"".join(analog_values_inverted))