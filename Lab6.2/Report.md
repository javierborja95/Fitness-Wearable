Javier Borja
PID: A15721796

Partner: Ron Rubio

# Lab 6.2

## Introduction
In this lab we continue with machine learning and its application to our heart rate IR circuit. We will utilize the previous lab's heart rate detection machine learning algorithm and expand on it. We will also classify different people based on their heart rate. We will then explore IMUs.

## Objective 1
*We will reuse our heart rate machine learning algorithm to plot live heart rates and display a user's heart rate live on the arduino device using the OLED display.*

#### Part A
* Modularize lab 6.1's hr detector.
    * Create my_hr_calculator.py that contains functions that fit a GMM to training data, makes label predictions on that training data, and calculates the heartrate on a new set based on the label predictions.
 #### Part B
* Create live_hr_monitor.py to calculate heartrate and send to the arduino.
    * Use Part A's functions to calculate the heart rate.
    * COllect a few second's worth of IR data, and create labels.
    * Calculate the heartrate by predicting on new 1 second data intervals.
* Create HRDisplay.ino to display the heartrate live on the arduino OLED display.

[Youtube video of OLED heartbeat](https://youtu.be/dxVj6_oqb88)


## Objective 2
*We will attempt to classify different users based on their heart rate data. We will use Supervised Learning and the K-nearest neighbor algorithm. Data points that are near each other will be labeled as one group and data points near each other in another locatin will be labeled as another group.*

* Using the heart rate deteector, collect 30-45 seconds of heart rates of two users.
    * We first data point of heart rate was the hollistic average, every data point afterwards was a 3 point moving average.
* Make a module knn_user_class.py that collects heart rates and time stamps into arrays.
* Apply the KNN algorithm to the data to train the classifier. 
* Load valid_hr data and predict the users based on the KNN labels.
    * Concatenate both sets and plot them.
* Compare to actual data and print out the accuracy of KNN.

![Objective2](/Lab6.2/Images/obj2.png)



## Objective 3
*We explore an IMU or inertial measurement unit. Our module contains a 3-axis accelerometer and a 3-axis gyroscope and we plot them while walking. We can use the results to our advantage by possible creating a stepcounter and other applications.*

* Use the wiring diagram to wire the MPU6050 module to its appropriate pins.
* Use and understand the sample code and use serial plotter to observe the effects of different movements.
    * This peripheral communicates via I2C. Each axis value is made of 2 byte chunks, so we must allocate 14 registers (2 extra for a temperature sensor).

![Objective3](/Lab6.2/Images/gyro.png)
* Only output the 3 gyro axes.

![Objective3](/Lab6.2/Images/accel1.png)
* Only output the 3 accelerometer axes.

a. The gyro and accer outputs differ based on what movements you make. Sharp sudden movements create spikes, while gentle movements create curves. Spinning created a sinusoidal signal on some different axes and lowering and raising the arm holding the device would smoothly transition values.
b. The ax and zx axes contains the most relevant data because if we make a pedometer that attaches to an arm, then those axes would have the biggest changes per movement. This is because the arm moves back and forth, and raises and lowers like a pendulum.
c. We could avoid extraneous data by appling a high pass filter, considering that walking has a very large period compared to sudden movements' signals.

## Objective 4
*In this lab we note that walking has a large period and is rhythmic. So we will plot its raw data and create a power spectral density (PSD) plot to see which frequencies are common in a walking motion. We will update these results on a live plot.*

* Use previous BLE code and combine with Objective 3's sample code to send single axes's IMU data to python at a frequency of 20 Hz.
* Collect the data in a python module.
* Use the Welch function on the incoming signal to generate the PSD plot.
* Use the animation module to plot the raw data and the updating PSD plot.

[Youtube video of IMU](https://youtu.be/9Raquad6Tlg)

In my experience, the data was similar in all the axis. But the signal was obviously periodical in all the plots. As we continue walking, the PSD has less "noise" and some peaks in the graph become more pronounced. We can use these peaks to somehow detect the period of our walking motion.


## Conclusion
* All parts of the lab went smoothly except for the some aspects of the IMU. One of my axes did not work, and my parter's did not work at all. It was difficult to observe useful data from the PSD plot, the raw signal looked better, as each step was clearly discernible.*
