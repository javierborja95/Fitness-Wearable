# Imports
import numpy as np
import scipy.signal as sig

# Globals
LP_b, LP_a, HP_b, HP_a = [],[],[],[]
LP_Zi, HP_Zi = [],[]

#####################################################################################

# Function to initialize and setup the filters

# Inputs: None
# Return: None

def setupFilters():
    global LP_b, LP_a, LP_Zi, HP_b, HP_a, HP_Zi

    LP_b, LP_a = sig.butter(3,10/100,btype='low',analog=False,output='ba')
    HP_b, HP_a = sig.butter(3,.5/100,btype='high',analog=False,output='ba')
    LP_Zi=sig.lfilter_zi(LP_b,LP_a)
    HP_Zi=sig.lfilter_zi(HP_b,HP_a)
    
    return

#####################################################################################

# Function to accept data and process it.
# This is the primary function of this module

# Inputs: np array dataIn, containing input data
# Return: np array dataOut, containing processed data

def processData(dataIn):
    global LP_b, LP_a, LP_Zi, HP_b, HP_a, HP_Zi

    # Here is the rough pseudocode:

    # 1. Use LP_b, LP_a, and LP_Zi to LPF data. Collect data_LP, new LP_Zi.
    # 2. Use HP_b, HP_a, and HP_Zi to HPF data. Collect data_HP, new HP_Zi.
    # 3. Return data_HP as dataOut.
    data_LP, LP_Zi = applyLPF(LP_b, LP_a, dataIn, LP_Zi)
    data_HP, HP_Zi = applyHPF(HP_b, HP_a, data_LP, HP_Zi)
    
    return data_LP

#####################################################################################

# Function to convert the ADC value(0-1023) to Voltage values(0-5V)
# Step 1 in processData()

# Inputs: dataIn, an np array containing ADC data
# Return: dataOut, the modified output np array containing voltage values

def adc2voltage( dataIn ):
    for i in range (len(dataIn)):
        dataIn[i]=(dataIn[i])*5/1023
        
    return dataIn

#####################################################################################

# Function to apply LPF
# Step 1 in processData()

# Inputs: np arrays LP_b, LP_a, dataIn, LP_Zi
# Return: np array dataOut, LP_Zi
# Use lfilter()

def applyLPF(LP_b, LP_a, dataIn, LP_Zi):
    return sig.lfilter(LP_b,LP_a,dataIn,-1,LP_Zi)

#####################################################################################

# Function to apply HPF
# Step 2 in processData()
# Use lfilter()

# Inputs: np arrays b, a, dataIn, Zi*dataIn[0]
# Return: np array dataOut, HP_Zi
def applyHPF(HP_b, HP_a, dataIn, HP_Zi):
    return sig.lfilter(HP_b,HP_a,dataIn,-1,HP_Zi*dataIn[0])

#####################################################################################