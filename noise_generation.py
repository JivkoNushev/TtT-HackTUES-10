import numpy as np
import random

def combine_noise_files(files):
    pass

def create_propeller_noise():
    # < 1000
    pass

def create_random_noise():
    fs = 100
    
    frequencies = []
    for i in range(random.randint(0, 100)):
        frequencies.append(random.randint(20, 20000))

    x = np.arange(fs) # the points on the x axis for plotting

    # compute the value (amplitude) of the sin wave for each sample
    random_waves = []
    for f in frequencies:
        random_waves.append(list(np.sin(2*np.pi*f * (x/fs))))

    # #Plot the sine waves

    #Adds the sine waves together into a single complex wave
    combined_waves = []
    for i in range(len(random_waves[0])):
        data = 0
        for ii in range(len(random_waves)):
            data += random_waves[ii][i]
        combined_waves.append(data)

    import matplotlib.pyplot as plt
    
    fig, c1 = plt.subplots()
    c1.plot(combined_waves, color="blue")

    plt.show()
    

def create_noise():
    propeller_noise = create_propeller_noise()
    random_noise = create_random_noise()

    return combine_noise_files([propeller_noise, random_noise])


create_random_noise()
