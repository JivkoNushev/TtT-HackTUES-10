from plot import *

plot_single_file('sample_audio/output.wav')
plot_single_file('sample_audio/output_inverted.wav')

plot_multiple_files(['sample_audio/output.wav', 'sample_audio/output_inverted.wav'])

plt.show()
