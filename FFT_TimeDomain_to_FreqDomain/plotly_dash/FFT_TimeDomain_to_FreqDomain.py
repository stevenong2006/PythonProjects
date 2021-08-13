import numpy as np
import pandas as pd
from icecream import ic
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# How many time points are needed i,e., Sampling Frequency
samplingFrequency   = 100

# At what intervals time points are sampled
samplingInterval       = 1 / samplingFrequency

# Begin time period of the signals
beginTime           = 0

# End time period of the signals
endTime             = 5

# Frequency of the signals
signal_4Hz     = 4 #Sine wave 1 = 4Hz
signal_7Hz     = 7 #Sine wave 2 = 7Hz
signal_9Hz     = 9 #Sine wave 3 = 9Hz

df = pd.DataFrame()
df["Time"] = np.arange(beginTime, endTime, samplingInterval)

# Create sine waves
df['4Hz'] = np.sin(2 * np.pi * signal_4Hz * df["Time"])
df['7Hz'] = np.sin(2 * np.pi * signal_7Hz * df["Time"])
df['9Hz'] = np.sin(2 * np.pi * signal_9Hz * df["Time"])

fig_4Hz = px.line(
    df, x="Time", 
    y="4Hz", 
    title='4Hz Sine wave',
    labels={
        'Time':'Time period',
        '4Hz':'Amplitude'
    },
    height=300,
    )
fig_7Hz = px.line(
    df, 
    x="Time", 
    y="7Hz", 
    title='7Hz Sine wave',
    labels={
        'Time':'Time period',
        '7Hz':'Amplitude'
    },
    height=300,    
    )

fig_9Hz = px.line(
    df, 
    x="Time", 
    y="9Hz", 
    title='9Hz Sine wave',
    labels={
        'Time':'Time period',
        '9Hz':'Amplitude'
    },
    height=300,    
    )
fig_9Hz.update_layout(height=300,)

df['sum_of_waveform'] = df['9Hz'] + df['7Hz'] + df['4Hz']

fig_sum_of_waveform = px.line(
    df, 
    x="Time", 
    y="sum_of_waveform", 
    title='Sum of 4Hz, 7Hz, and 9Hz Waveforms as Input into FFT',
    labels={
        'Time':'Time period',
        'sum_of_waveform':'Amplitude'
    },
    height=300,    
    )
#--- Transform from time domain to frequency domain ---#

# Frequency domain representation
fourierTransform = np.fft.fft(df['sum_of_waveform'])/len(df['sum_of_waveform'])           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(df['sum_of_waveform'])/2))] # Exclude sampling frequency

tpCount     = len(df['sum_of_waveform'])
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency

FFT_df = pd.DataFrame()

FFT_df["frequencies"] = values/timePeriod

FFT_df["realFourierTransform"] = abs(fourierTransform)

arrFreq = np.array([FFT_df["frequencies"], FFT_df["realFourierTransform"]])

# dim, totalElements = arrFreq.shape

#print(f'dim={dim}, totalElements={totalElements}')

print(f'Found the following fequencies after transformation: ')
str = 'Detected the following fequencies in frequency domain:'
for i, j in np.argwhere(arrFreq > 0.495):
    if i > 0:
        print(f'{j/endTime} Hz ') # since time period = (start, end), and freq is recipical of time ---> 1/t
        str +=  f' {j/endTime} Hz,'

str = str[:-1]


# frequencies = values/timePeriod
# realFourierTransform = abs(fourierTransform)

fig_frequency_domain = px.line(
    FFT_df, 
    x="frequencies", 
    y="realFourierTransform", 
    title='Frequency Domain Waveform',
    labels={
        'frequencies':'Frequency (Hz)',
        'realFourierTransform':'Amplitude'
    },
    height=300,    
    )

fig_frequency_domain.update_layout(hovermode="x")



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.H6(
        'FFT - Time Domain to Frequency Domain Transformation Demonstration',
        style={
            'textAlign': 'center',
        }
        ),
    html.Div([
        html.Div([
            html.Div(children='''
                Sinusoidal waveforms frequencies 4Hz, 7Hz, and 9Hz repectively
            '''),

            dcc.Graph(
                id='graph1',
                figure=fig_4Hz
            ),  
        ], className='row'),
        html.Div([
            dcc.Graph(
                id='graph2',
                figure=fig_7Hz
            ),  
        ], className='row'),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=fig_9Hz
            ),  
        ], className='row'),        
    ], className='row'),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        dcc.Graph(
            id='graph4',
            figure=fig_sum_of_waveform
        ),  
    ], className='row'),
    html.Div([
        html.H5(str, style={'textAlign': 'center',}),        
        dcc.Graph(
            id='graph5',
            figure=fig_frequency_domain
        ),  
    ], className='row'),
    
])

if __name__ == '__main__':
    app.run_server(debug=True)