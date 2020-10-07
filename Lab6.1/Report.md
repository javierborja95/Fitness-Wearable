Javier Borja
PID: A15721796

Partner: Ron Rubio

# Lab 6.1

## Introduction
In this lab we utilize machine learning to detect heartbeats.We will create labels of heartbeats and not heartbeats. Then we develop an algorithm using our machine learning data to calculate heart rate.

## Objective 1
*We will acquire raw heartbeat data for our machine learning algortithm. We will then analyze this data in two sets: a training set and validation set.*

* Create an arduino sketch that will capture raw hearbeat data and will send it to python with a timestamp.
* Create a python module that will collect 30-45 seconds of raw data and save it to a file.
* Create python modules that will plot 5 seconds of raw signal, and create a python module that will plot 5 seconds of a filtered signal.

![Objective1](/Lab6.1/Images/Obj1_Signals.png)

* Split the raw data into a training and validation set.
    * We split it 70/30.
* Plot the IR signal into a histogram with 50 bins.

![Objective2](/Lab6.1/Images/Obj1_Hist.png)

* You can easily see there would be two classes.
    * The first class would be most of the signal when there is no heartbeat, the second class would be some of the signal when there is a heartbeat.


## Objective 2
*We will use our histogram and apply the technique of an unsupervised machine learning algorithm. This will be done to split the data into two classes: heartbeat or not a heartbeat.*

* Use reference material and apply a 2-component Gaussian mixture model to training data set.
* Create a normalized histogram with the sum of two Gaussians.
![Objective2](/Lab6.1/Images/Obj2_SumGaus.png)

* Create a nomalized histrogram with the two Gaussians.
![Objective2](/Lab6.1/Images/Obj2_TwoGaus.png)

    * We used mean, covariance, and weight parameters.

* Use predict() to label the training set and validation set.
* Plot the data.
![Objective2](/Lab6.1/Images/Obj2_TrainPredictions.png)
![Objective2](/Lab6.1/Images/Obj2_ValidPredictions.png)
* Export both data sets into train_predictions and valid_predictions.
    * The data will contain vectors with < raw IR value, timestamp, label>.



## Objective 3
*Use the predicted labels to calculate heart rate of training set and validation set. We must develop an algorithm to detect a heartbeat and rid of mislabeled heartbeats.*

* Apply the heartbeat detector algorithm to detect heartbeats.
    * Our algorithm differentiated between labels. A 1 label was a heartbeat and a 0 label was not a heartbeat. We counted the time a hearbeat lasted and the time between each heartbeat. All heartbeats were displayed a label of 1 but there were some small signals that were large enough to be labeled a heartbeat, but not actual heartbeats.
    * To rid of mislabeled heartbeats we averaged the time each heartbeat occured. If the label fell below some threshhold, then it was removed. This would remove smaller signals that were incorrectly labeled. We also took the average between each heartbeat. If the label came significantlly earlier, then that meant it was due to the little pulse behind the actual heartbeat that was incorrectly counted as a heartbeat, and that the other technique did not remove.
    * We also noticed that it was possible for our algorithm to remove shorter pulses if they occured at the beginning and in the middle of a pulse, or the end of the data set and did not finish before the data set ended. We accounted for these possibilities in pur algorithm.
* Calculate the holistic heart rate.
* Plot the 3-beat moving average heart rate.

* Do for both the training set and validation set.

![Objective3](/Lab6.1/Images/train_hr.png)
    * The green dots represent a valid heartbeat. Our algorithm detected a single bad heartbeat that occured at the beginning and removed it.


![Objective3](/Lab6.1/Images/valid_hr.png)
    * It worked for our validation set as well.

## Conclusion
* This lab went very smoothly. The only diffulties were learning how to apply gaussians and developing an algorithm to detect erroneous heartbeats. There was no problem applying the algorithm.*
