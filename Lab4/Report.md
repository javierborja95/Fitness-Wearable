Javier Borja

A15721796

# Lab 4

## Introduction
The objective for lab 4 is to develop a heartbeat display by creating an IR circuit. We will use IR components to read our pulses and we will apply amplification circuits, digital filters, and transformations to clean our heartbeat signal for easy visuilization on our OLED.

## Objective 1
*We created a IR emitter and reciever circuit. We turned on a IR led and connected an IR reciever with a capacitor to smooth the induced voltage from the reciever. This induced voltage represented our pulse. We then applified our signal by using an OpAmp applifier circuit.*

#### Part A
* Connect the IR emmiter to 5V in series with 220 ohm resisitor.
* Ground an IR reciever in series with a 10k resistor connected to 5V. Then in the node between the resistor and reciever connect a 1 microfarad capacitor, this is our output. 
![Circuit1](/Lab4/Images/circuit1.jpg)
* Test the signal with an Arduino sketch to read values and plot it on Serial Plotter.

![Objective1](/Lab4/Images/1a.png)

#### Part B
* Add an amplifier circuit
    * Connect an LM386 OpAmp
    * Put a 100 microfarad capacitor in pins 1 and 8.
    * Ground pins 2 and 4
    * Connect 5V to pin 6
    * Connect pin 3 to a node with a grounded 100k resistor and another 100k resistor connected to the old output.
    * New outout is pin 5.
![Circuit2](/Lab4/Images/circuit2.jpg)

![Objective1](/Lab4/Images/1b.png)

*The amplifier fixed the choppiness of the signal by increasing the range of the signal to reduce the effect of quantization of the output voltage. The amplifier lets us see more detail in the incoming signal.*


## Objective 2
*In this objective we will apply digital filters to smooth our signal and we will apply transformations to see a cleaner signal representing heartbeat pulses.*

#### Part A
* Use Arduino filters to apply one pole and two pole Low-pass filters.
    * Set the cutoff frequency of 2.0 Hz
* Compare the One pole and two pole filters.

![Objective2](/Lab4/Images/2a1_2hz.png)
![Objective2](/Lab4/Images/2a2_2hz.png)
* The first is the one pole low pass filter and the second is the two pole low pass filter. The two pole signal seems slightly more smooth due to the inductor effect. Inductors oppose the change in current, and we can see that by a smoothing of a signal.

*Increasing the cutoff frequency allowed more signal to pass, and decreasing the cutoff frequency decreased the detail of the signal.*

#### Part B
* Use a derivative transformation to the signal.
![Objective2](/Lab4/Images/2b_derivative.png)

* Apply two of your own transformations.
![Objective2](/Lab4/Images/2b_2pLpfD.png)
*I use a low pass filter to smooth the signal and I applied a derivative to it to so you can easily see spikes representing a tick of a heartbeat.*
![Objective2](/Lab4/Images/2b_2pLpfDLpf.png)
*I took the above signal and made it sinusioudal-like by applying a second low pass filter the the derivative. This was done in preperation for the heartbeat sensor. Sinusioidal signals make easy to see on the OLED display. I also truncated the lowest values as they are not needed to see a heartbeat.*

## Objective 3
*In this objective we attached our heartbeat detector to different parts of our body to see how they are displayed relative to each other to choose the best place to put our detector.*

* Attach jumper wires to the IR emmiter and reciever.
* Attach them to your fingertip, wrist, and our own choice.

![Objective3](/Lab4/Images/3a.png)
*This signal from our finger tip is very reliable and works. Spreading the receiver and emitter to the tip and to the crease of the finger seems to increase the effect of the heartbeat signal.*
![Objective3](/Lab4/Images/3b.png)
*The wrist was very difficult to get any consistant signal. Increasing or decreasing the distance didn't seem to have a significant effect on the signal.*
![Objective3](/Lab4/Images/3c.png)
*This signal is from my lip. I chose this place because this part of the body is thin and changes in bloodflow would have been easy to detect. One disadvantage of this placement is the unsanitary aspect of this.*

## Objective 4
*This objective's purpose was to display our plot into a easy to see display on our OLED. We will map our transformed signal and map it into a shape. We will also take our data and transfer the raw numbers into our computer via BLE.*

#### Part A
* Take your transformed signal and apply a mapping function to it.
    * I cut off the top and bottom of a transformed sinusioidal-like signal and mapped it into a circle representing a max and min of a pulse signal.
    * My mapping equation consisted of mapping a 0-radius value. I calculated a range by doing the highest allowed value minus the lowest allowed value. These allowed values were determined by my calibration function. Then I multiplied the radius times the input value minus the lowest value all divided by the range, so I could get a 0-1 mapping, with 1 representing the max value or filling up the entire circle.

[Youtube video of OLED heartbeat](https://youtu.be/JbeK9cx6kpU)

#### Part B
* Modify part A to include sending the raw data over BLE.
* Create a python sketch to collect the incoming data for 20 seconds.
* Plot the data.
* Have the arduino BLE module sleep when pressing the button, so connect the arduino to a 9V battery.

## Conclusion
* I had trouble with objective 4, specifically, objective B. My problem was that the arduino would not send quick enough. If my collection time was lower, then the serial buffer would have enough data to compensate for the incoming data that wouldn't be enough by itself. A sample of my raw data is included in raw_data.npy. The inputs get messed up as the collection nears the end. I could not fix it in by the time of submission. Overall, the rest of the lab went pretty smoothly. It was interesting to see the effect of some filters to the signal.*
