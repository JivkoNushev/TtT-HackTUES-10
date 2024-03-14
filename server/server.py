import sys
import wave
import scipy.io.wavfile
import paho.mqtt.client as paho

NUM_SAMPLE_BYTES_TO_WRITE = 10
SAMPLE_RATE = 44100
SAMPLE_RATE = 1
SAMPLE_WIDTH = 1 << 16 - 1
SAMPLE_WIDTH_BYTES = 2


def dysect(fileName):
    output = []

    wavfile = scipy.io.wavfile.read(fileName)

    output.append(wavfile)
    return output # returns opened scipy wav files (not wave)

    # print(wavfile)
    # fs, data = wavfile.read('test.wav') # load the data
    # a = data.T[0] # this is a two channel soundtrack, I get the first track
    # b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    # c = fft(b) # calculate fourier transform (complex numbers list)
    # d = len(c)/2  # you only need half of the fft list (real signal symmetry)
    # plt.plot(abs(c[:(d-1)]),'r')
    # plt.show()

def choose_from_dysected(dystected_files):
    return dystected_files[0]

def combine(files):
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

def message_handling(client, userdata, msg):
    msg_str = msg.payload.decode()
    li = list(msg_str[1:-1].split(", "))
    li_bytes = []
    timestamp = li[0]
    li = li[1:]
    for num in li:
        li_bytes.append(int(num).to_bytes(2, "little", signed=True))
    print(li_bytes)
    client.publish("silence", msg.payload.decode(), 0)

    file_name = "sample_audio/output.wav"

    wav_file = wave.open(file_name, "w")
    wav_file.setnchannels(1)
    wav_file.setsampwidth(SAMPLE_WIDTH_BYTES)
    wav_file.setframerate(SAMPLE_RATE)

    wav_file.writeframes(b"".join(li_bytes))

    sample_rate_output1 = wav_file.getframerate()

    wav_file.close()

    dysected_files = dysect(file_name)
    chosen_files = choose_from_dysected(dysected_files)
    combined = combine(chosen_files)

    # combine chosen_files
    sample_rate_output2, bulshit = scipy.io.wavfile.read(file_name)
    print(sample_rate_output1, sample_rate_output2)
    scipy.io.wavfile.write('sample_audio/combined.wav', sample_rate_output2, -combined)


client = paho.Client()
client.on_message = message_handling

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.subscribe("noise")

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except Exception:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()
