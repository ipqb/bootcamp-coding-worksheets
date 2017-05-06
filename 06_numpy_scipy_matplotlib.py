# Intro to NumPy, SciPy, and Matplotlib
# For this intro to numerical/scientific computing and plotting, you will
# write code to generate a decaying sine-wave signal with noise and plot the
# average over repeat measurements.
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt


def generate_time_values(duration, spacing):
    """Get an array of measurement times."""
    return []


def generate_sine_wave(time, peak, freq=1.):
    """Generate a sine wave with provided amplitude and frequency."""
    return []


def generate_decay(time, data, decay_rate=.1):
    """Given a signal, decay the signal with an exponential function.

       e.g. f(x, k, t) = x e^(-k t)
    """
    return []


def generate_noise(data, sigma=.05):
    """Real data is noisy. Add simulated noise to the data."""
    return []


def generate_wave(sample_freq=100., wave_freq=1., peak=1., duration=50.,
                  decay_rate=.1, sigma=.05):
    """Generate noisy decaying wave with provided parameters."""
    return [], []


def plot_wave(time, data):
    """Plot wave."""
    pass


def generate_multiple_waves(n=10):
    """Generate multiple noisy decaying waves with shared sample times."""
    return [], [[]]


def calculate_data_statistics(data_array):
    """Calculate mean and standard deviation across repeated measurements."""
    return [], []


def plot_waves_and_statistics(time, wave_array, mean_wave, std_wave):
    """Plot all repeats of waves with mean and confidence interval.
       Note: focus here on making a plot that is visually interpretable."""
    pass


# part 1: Generate noisy decaying wave. Feel free to play with parameters.
time, wave = generate_wave()

# part 2: Plot wave
plot_wave(time, wave)

# part 3: Generate many waves and place in one array
n = 10
time, wave_array = generate_multiple_waves(n)

# part 4: Compute wave statistics (mean and standard deviation)
mean_wave, std_wave = calculate_data_statistics(wave_array)

# part 5: Plot waves with wave statistics
plot_waves_and_statistics(time, wave_array, mean_wave, std_wave)
 
## Bonus: For prettier plots, uncomment the following block and place at the
## top. For less clutter, add `sns.despine()` before `plt.show()`
# import seaborn as sns
# sns.set_style("white")
    
