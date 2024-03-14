import sys
import wave
import scipy.io.wavfile
import paho.mqtt.client as paho

NUM_SAMPLE_BYTES_TO_WRITE = 10
SAMPLE_RATE = 44100
SAMPLE_RATE = 1
SAMPLE_WIDTH = 1 << 16 - 1
SAMPLE_WIDTH_BYTES = 2


def fourier(wavfile):
    print(wavfile)
    # fs, data = wavfile.read('test.wav') # load the data
    # a = data.T[0] # this is a two channel soundtrack, I get the first track
    # b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    # c = fft(b) # calculate fourier transform (complex numbers list)
    # d = len(c)/2  # you only need half of the fft list (real signal symmetry)
    # plt.plot(abs(c[:(d-1)]),'r') 
    # plt.show()
    

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
    
    wav_file = wave.open("sample_audio/output.wav", "w")
    wav_file.setnchannels(1)
    wav_file.setsampwidth(SAMPLE_WIDTH_BYTES)
    wav_file.setframerate(SAMPLE_RATE)
    wav_file.writeframes(b"".join(li_bytes))
    
    sample_rate_output, output = scipy.io.wavfile.read('sample_audio/output.wav')
    output = -output
    scipy.io.wavfile.write('sample_audio/combined.wav', sample_rate_output, output)
    proppeler = fourier(wav_file)



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
