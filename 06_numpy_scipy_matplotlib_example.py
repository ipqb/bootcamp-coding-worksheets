# Intro to NumPy, SciPy, and Matplotlib
# For this intro to numerical/scientific computing and plotting, you will
# write code to generate a decaying sine-wave signal with noise and plot the
# average over repeat measurements.
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style("white")


def generate_time_values(duration, spacing):
    """Get an array of measurement times."""
    return np.linspace(0, duration, duration / spacing)


def generate_sine_wave(time, peak, freq=1.):
    """Generate a sine wave with provided amplitude and frequency."""
    return peak * np.sin(freq * time)


def generate_decay(time, data, decay_rate=.1):
    """Given a signal, decay the signal with an exponential function.

       e.g. f(x, k, t) = x e^(-k t)
    """
    return data * np.exp(-decay_rate * time)


def generate_noise(data, sigma=.05):
    """Real data is noisy. Add simulated noise to the data."""
    return data + np.random.normal(0, sigma, size=data.size)


def generate_wave(sample_freq=100., wave_freq=1., peak=1., duration=50.,
                  decay_rate=.1, sigma=.05):
    """Generate noisy decaying wave with provided parameters."""
    time = generate_time_values(duration, duration / sample_freq)
    sin_wave = generate_sine_wave(time, peak)
    decay_wave = generate_decay(time, sin_wave, decay_rate=decay_rate)
    noisy_wave = generate_noise(decay_wave, sigma=sigma)
    return time, noisy_wave


def plot_wave(time, data):
    """Plot wave."""
    plt.plot(time, data)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    sns.despine()
    plt.show()


def generate_multiple_waves(n=10):
    """Generate multiple noisy decaying waves with shared sample times."""
    time = None
    waves = []
    for i in range(10):
        time, wave = generate_wave()
        waves.append(wave)
    waves = np.array(waves, dtype=np.float)  # turn list of 1D arrays to 2D array
    return time, waves


def calculate_data_statistics(data_array):
    """Calculate mean and standard deviation across repeated measurements."""
    return np.mean(data_array, axis=0), np.std(data_array, axis=0)


def plot_waves_and_statistics(time, wave_array, mean_wave, std_wave):
    """Plot all repeats of waves with mean and confidence interval.
       Note: focus here on making a plot that is visually interpretable."""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(wave_array.shape[0]):
        ax.plot(time, wave_array[i, :], alpha=.2, color='k', zorder=0)
    ax.fill_between(time, mean_wave - std_wave, mean_wave + std_wave,
                    alpha=.35, color='b', zorder=1)
    ax.plot(time, mean_wave, color='k', zorder=2)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    sns.despine()
    plt.show()


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
