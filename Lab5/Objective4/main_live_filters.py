# Imports
import ece16ble as bt
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import ece16anims as an
import ece16filters as fl

# Global variables
serial_port = "/dev/ttyACM1"
peripheral_MAC = "A810871B48DE"
#peripheral_MAC = "6CC374FCAD6F"
N = 400                                         # samples to plot
NS = 20                                         # samples to grab each iteration

times = []
values, values2, live_plots= [],[],[]

def first_filter():
    global LP_Zi, HP_Zi , times, values, values2
    # Read the first sample andmples) # show 1/4 of a period each cycle
    # Call adc2voltage to convert adc data to voltages. Get output in a variable.
    # LP_Zi = LP_Zi * data[0]
    # HP_Zi = HP_Zi * data[0]
    # Call processData() and pass the array as an input.
    times, values = an.grab_samples(NS)
    values=fl.adc2Voltage(values)
    LP_Zi = LP_Zi * values[0]
    HP_Zi = HP_Zi * values[0]
    values2=fl.processData(values)


def grab_and_filter():
    global LP_Zi, HP_Zi , times, values, values2
    # Read samples from serial and store it in an array.
    # Call adc2voltage to convert adc data to voltages. Get output in a variable.
    # Call processData() and pass the array as an input. Get output in a variable.
    
    times, values = an.grab_samples(NS)
    values=fl.adc2Voltage(values)
    values2=fl.processData(values)

    # shift samples left by 'NS'
    times[:N-NS] = times[NS:]
    values[:N-NS] = values[NS:]
    values2[:N-NS] = values2[NS:]

    # grab new samples
    times[N-NS:], values[N-NS:], values2[N-NS:] = an.grab_samples(NS)
    
    values[N-NS:]=fl.adc2voltage(values[N-NS:])
    values2[N-NS:]=fl.processData(values[N-NS:])

    # plot
    [ax.set_xlim(times[0],times[N-1]) for ax in axes]
    live_plots[0].set_data(times, values)
    live_plots[1].set_data(times, values2)

    return live_plots

# Main function
if(__name__ == "__main__"):

    # Set up the BLE code
    # Set up the animation code
    # Call the setupFilters function
    # Call the first_filter function
    # Call the processData function from within funcAnimation() as shown below:
    # anim = animation.FuncAnimation(fig, grab_and_filter, fargs=(data,), interval=500)

    try:
        bt.ble_setup( serial_port, peripheral_MAC )
        bt.ble_connect()
        
        # initialize the figure 
        fig, axes = plt.subplots(2, 1)
        times, values, values2 = an.grab_samples(N)
    
        live_plots.append(axes[0].plot(times, values, lw=2)[0])
        live_plots.append(axes[1].plot(times, values2, lw=2)[0])
    
        # initialize the y-axis limits and labels
        [ax.set_ylim(0, 5) for ax in axes]
    
        axes[0].set_title('Raw')
        axes[0].set_xlabel('Time (s)')
        axes[0].set_ylabel('Amplitude (V)')
    
        axes[1].set_title('Filtered')
        axes[1].set_ylabel('Amplitude (V)')
        axes[1].set_xlabel('Time (s)')
        
        fl.setupFilters()
        first_filter()
        
        #fl.setupFilters()
        anim=animation.FuncAnimation(fig,grab_and_filter(),interval=500)

    except Exception as e:
        print("Error: " + str(e))
        bt.ble_close()