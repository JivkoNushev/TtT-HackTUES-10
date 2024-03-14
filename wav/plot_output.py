from plot import *


files = [
        'sample_audio/1.wav',
        'sample_audio/2.wav',
        'sample_audio/main.wav',
        'sample_audio/combined.wav'
    ]

for file in files:
    plot_single_file(file)

plot_multiple_files(files)

plt.show()
