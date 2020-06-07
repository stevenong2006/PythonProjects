# Python example - Fourier transform using numpy.fft method

import numpy as np
import matplotlib.pyplot as plotter

# How many time points are needed i,e., Sampling Frequency
samplingFrequency   = 100

# At what intervals time points are sampled
samplingInterval       = 1 / samplingFrequency

# Begin time period of the signals
beginTime           = 0

# End time period of the signals
endTime             = 10

# Frequency of the signals
signal1Frequency     = 4 #Sine wave 1
signal2Frequency     = 7 #Sine wave 2
signal3Frequency     = 9 #Sine wave 3

# Time points
time        = np.arange(beginTime, endTime, samplingInterval)

# Create two sine waves
amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)
amplitude3 = np.sin(2*np.pi*signal3Frequency*time)

# Create subplot
figure, axis = plotter.subplots(5, 1)
figure.set_figwidth(12.8)
figure.set_figheight(9.6)
plotter.subplots_adjust(hspace=1)

# Time domain representation for sine wave 1
axis[0].set_title('Sine wave #1 with a frequency of 4 Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')
axis[0].set_xticks([0,1,2,3,4,5,6,7,8,9,10])

# Time domain representation for sine wave 2
axis[1].set_title('Sine wave #2 with a frequency of 7 Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')
axis[1].set_xticks([0,1,2,3,4,5,6,7,8,9,10])

# Time domain representation for sine wave 2
axis[2].set_title('Sine wave #3 with a frequency of 9 Hz')
axis[2].plot(time, amplitude3)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')
axis[2].set_xticks([0,1,2,3,4,5,6,7,8,9,10])
 

# Add the sine waves -- plot the 2 sine waves as one graph
amplitude = amplitude1 + amplitude2 + amplitude3

# Time domain representation of the resultant sine wave
#axis[2].set_title('Sine wave with multiple frequencies')
axis[3].set_title('Signals of Sine Waves 1, 2, and 3 Combined in One Graph')
axis[3].plot(time, amplitude)
axis[3].set_xlabel('Time')
axis[3].set_ylabel('Amplitude')
axis[3].set_xticks([0,1,2,3,4,5,6,7,8,9,10])

#--- Transform from time domain to frequency domain ---#

# Frequency domain representation
fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency

tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

realFourierTransform = abs(fourierTransform)
#print(f'{realFourierTransform}')

arrFreq = np.array([frequencies, realFourierTransform])

dim, totalElements = arrFreq.shape

#print(f'dim={dim}, totalElements={totalElements}')

print(f'After FFT, found the following freq at: ')
for i, j in np.argwhere(arrFreq > 0.495):
    if i > 0:
        print(f'{j/10} Hz ') # since (start, end) = 10, and freq is recipical of time ---> 1/t 

"""
Tested on 05/31/2020

After FFT, found the following freq at:
4.0 Hz
7.0 Hz
9.0 Hz

"""

 
# Frequency domain representation
axis[4].set_title('Fourier transform depicting the frequency components')
axis[4].plot(frequencies, abs(fourierTransform))
axis[4].set_xlabel('Frequency')
axis[4].set_ylabel('Amplitude')
axis[4].set_xticks([0,1,2,3,4,5,6,7,8,9,10,15,20,25,30])

plotter.show()