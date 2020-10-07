# Imports
import ece16filters as fl
from matplotlib import pyplot as plt
import numpy as np

# Main function
if(__name__ == "__main__"):
    
    fl.setupFilters()
    
    
    # Read data and load into an np array
    a=[]
    
    f=open('raw_data.npy','r')
    lines = f.readlines()
    for line in lines:
        a.append((float(line)))
    f.close()
    
    # Call adc2voltage function
    a=fl.adc2voltage(a)
    arr=np.array(a)
    
    # Plot the data received
    plt.figure(figsize=(8,6), dpi=80)
    plt.subplot(211)
    plt.plot(arr, color="blue", linewidth=1.0, linestyle="-")
    plt.yticks(np.linspace(0,5,6,endpoint=True))
    plt.xticks()
    plt.ylabel("voltage(V)")
    plt.xlabel("Raw signal")
    
    # Call the processData function
    arr=fl.processData(arr)
    
    #Plot filtered data
    plt.subplot(212)
    plt.plot(arr, color="blue", linewidth=1.0, linestyle="-")
    plt.yticks(np.linspace(0,5,6,endpoint=True))
    plt.xticks()
    plt.ylabel("voltage (V)")
    plt.xlabel("Filtered Signal")   
    # Show result on screen
    plt.show()