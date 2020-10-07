Javier Borja
PID: A15721796

Partner: Ron Rubio

# Lab 7

## Introduction
In this lab we continue using our IMU to develop a step counter. We use a peak detection and moving average algorithm and decide if a user is actively walking. We then apply our own improvements to this method. We also learn the basics of a vibrating motor so we can include haptic feedback on future works.

## Objective 1
*We explore some ways we can use our IMU data. We use an L1 norm to minimize loss of information and so that we use information from all the axes, and we clean up the signal by processing it through a filter.*

#### Part A
* Use the previous lab's arduino code to send IMU data.
    * Use the L1 norm, which is the sum of the absolute values of the all the acceleration axes.
* Use a low pass filter with a cutoff of 4Hz.
    * Half of our sampling frequency of 20 Hz is 10 Hz so using the Nyquist frequency of the filter is 0.4 .
* Display the live plot of the raw signal and filtered signal

![Objective1](/Lab7/Images/Objective1.png)


## Objective 2
*We will attempt to create a step detector by detecting peaks of the IMU signal and by finding the moving average of these.*

* Invert the IMU acceleration signal by subracting it from the max of 3*16384, each step will have a peak.
    * This is due to the natural acceleration from a swinging arm; It speeds up as it reaches the bottom of a swing.
* Send IMU data to python and create a function pedometer() that finds the max value of the past 10 samples and then the previous 10 samples.
    * Store each of these max values into an array along with its timestamp.
* Keep the size of the array 20 items long by deleting the oldest values while adding in new ones.
* Plot the moving average values and note the values of a stationary and flat IMU
versus an actively walking motion.
![Objective2](/Lab7/Images/Objective2.png)



## Objective 3
*We use our previously defined moving average filter output to classify steps for our counter. We note a user as active and see whether their IMU signals fall within a certain range, which we will count as a step event. Then we note that they have been active for a while and reduce the threshhold so that we don't restart the active process if they slow down for a moment.*

* Use the previously noted resting average of the IMU and use an upper threshold that is about 7000 more than it, to classify the user as active.
    * If the user was active, use the last two peaks to check if they were actually steps.
* Create a step variance of about 1300 below the moving average to see if the signals fall below it, so that we can classify each step.
* Classify about 5000 more than your resting IMU value as not active and the lower threshold of active walking.
* Increase the count of a counter when each step event is identified, and display live results to the OLED on the arduino.

[Objective3](https://youtu.be/c8r_RO57IyE)

## Objective 4
*In this objective we implement our own improvements to the step counter algorithm.*

* Using our previously defined step counter sketches and functins, include gyroscope data.
    * Just like the acceleration values, we create an upper threshold of gyroscope data because it contains peaks as well.
            * Incorperate it like the previous algorithm.
    * We also note that a wrist does not usually rotate while walking, but stays parallel to the plane of circular rotation.
            * If there is too much rotational motion like waving, then the "active" state is not walking.

[Objective4before](https://youtu.be/bGwhIWcoAME)

Our step counter before

[Objective4after](https://youtu.be/RwbYt9jhJSY)

And our step counter after

## Objective 4
*In this objective we explore another potential feedback mechanism for the user. Instead of displaying information to a user, we can use information to note the user by haptic feedback by the use of a vibrating motor.*

* Connect 5V to the motor and connect the ground to a digital pin.
    * Instead of connecting the red lead to a pin, we connect it to 5 V because the current output from a pin is less than the maximum current input to a pin.
    * We make the pin a current since because a lower current through the vibrating motor results in a very minimal effect.
* Create a sketch that turns on the motor with a LOW signal.
* This signal turns LOW twice after a randomly generated countdown from 1-10 reaches 0, then it repeats.

[Objective5](https://youtu.be/uikQzzaSMKA)

## Conclusion
* This lab went pretty straightforward with no problems. We will use our vibrating motor to enhance feedback perception for the user. We can also use our vibrating motor to maybe note a user when a step from our step counter is counted. We may also be able to use our IMU as some sort of crash or fall detector, or with some math we may use it as some sort of navigator as well.*
