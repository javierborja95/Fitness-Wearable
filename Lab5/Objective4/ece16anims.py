# Imports
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import ece16ble as bt

# Globals
N = 0                                         # samples to plot
NS = 0                                         # samples to grab each iteration
sample_count = 0                                # current sample count
times, values, values2 = [],[],[]               # data vectors
axes = []
live_plots = []

# Function to generate a number of samples
# Inputs: n_samples is the number of samples to be generated
# Return: np arrays for time, value1 and value2z
def grab_samples( n_samples ):
    global sample_count # using global variable 'sample_count'

    t, x, y = np.zeros( (3, n_samples) )
    for i in range(n_samples) :        
        t[i] = (sample_count + i) / (4 * n_samples) # show 1/4 of a period each cycle
        x[i] = bt.ble_read_line(" ")
        y[i] = x[i]

    sample_count += n_samples
    return t, x, y

# Grab new samples and plot
# Inputs: 
def update_plots(i):
    global times, values

    # shift samples left by 'NS'
    times[:N-NS] = times[NS:]
    values[:N-NS] = values[NS:]
    values2[:N-NS] = values2[NS:]

    # grab new samples
    times[N-NS:], values[N-NS:], values2[N-NS:] = grab_samples(NS)

    # plot
    [ax.set_xlim(times[0],times[N-1]) for ax in axes]
    live_plots[0].set_data(times, values)
    live_plots[1].set_data(times, values2)

    return live_plots

# Main
def init(total_samples, step_size):

    global N, NS, times, values, values2, axes
    N = total_samples
    NS = step_size
    times, values, values2 = np.zeros((3, N))       # data vectors

    # initialize the figure 
    fig, axes = plt.subplots(2, 1)
    times, values, values2 = grab_samples(N)

    live_plots.append(axes[0].plot(times, values, lw=2)[0])
    live_plots.append(axes[1].plot(times, values2, lw=2)[0])

    # initialize the y-axis limits and labels
    [ax.set_ylim(-1, 1) for ax in axes]

    axes[0].set_title('sin^2(t)')
    axes[0].set_xlabel('Time (s)')
    axes[0].set_ylabel('Amplitude')

    axes[1].set_title('cos^2(t)')
    axes[1].set_ylabel('Amplitude')
    axes[1].set_xlabel('Time (s)')

    # set and start the animation and update at 1ms interval (if possible)
    anim = animation.FuncAnimation(fig, update_plots, interval=500)
    plt.show()
    return