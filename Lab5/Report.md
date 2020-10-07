Javier Borja

A15721796

# Lab 5

## Introduction
The objective for lab 5 is to expand on our arduino to python data transmition to process and plot it live using numpy and scipy for digital signal processing.

## Objective 1
*We cleaned and modularized our existing code so that we can have a library of modules and keep our main code at a minumum and easy to read.*

* Download ece16bt.py and main_bt.py
* Fill in the defined functions in ece16bt.py with our existing code.
* Use main_bt.py to test our modified ece16bt.py
* use old arduino code to recieve data from python.

[Objective1 youtube video](https://youtu.be/mWu3cSMnnWs)

## Objective 2
*In this objective we will use pyplot to create graphs and plot signals to replace the Arduino's Serial plotter. We then plotted live signals in an animated graph using matplotlib's animation library.*
#### Part A
* Download and understand the pyplot_basics.py sample code
    * It initialized the plot and set the x points linespace. It graphed y as a function of x and plotted it.
* Use the sample code to create plots.py, which includes a cosine and sine graph in a single plot.

![Objective2](/Lab5/Images/2a_plot.png)

* Use the sample code to create subplots.py which now seperates the two signals into two different subplots.

![Objective2](/Lab5/Images/2a_subplot.png)

#### Part B
* Download and understand the animation sample code.
    * The initial data is stored in arrays and each new sample shifts the data to the left.
* Modify the sample code to animate the graphs of sin^2(x) and cos^2(x) into seperate subplots.

![Objective2](/Lab5/Images/Objective2b.png)

## Objective 3
*The goal of this objective is to replace the Arduino filters to use efficient signal processing on python to apply low and high pass filters using scipy.*

* Download the psuedo code and modify ece16filters.py to apply a low pass filter with cutoff frequency of 10.0 Hz and a high pass filter with a cutoff frequency of .5 Hz.
* Use raw_data.np from previous lab and store it.
* Pass the data through the filters.
* Plot both the raw signal and the filtered signal.

![Objective2](/Lab5/Images/Objective3.png)


## Objective 4
*The purpose of objective 4 is collect data from the IR circuit, process it through python, filter it, and plot it live.*

* Create ece16filters.py that filters a signal according to our input parameters.
* Create main_live_filters.py
    * Have it receive data from the Arduino over BLE.
    * Have it call ece16filters.py to filter the incoming data.
    * Plot the raw signal and filtered signal live.

## Conclusion
*I could not finish objective 4 because of failure of my connection to the BLE module via my python computer. Even objective 1 could not be replicated again. I have included my code for objective 4 in its respective folder, but I could not verify the live animation module because I could not connect to the Arduino anymore. The rest of the lab went smoothly until I could not send AT commands to either of the HM-10 modules. I had to do a lot of reading of documentation to figure out objective 3 because the scipy modules were not intuitive.*
