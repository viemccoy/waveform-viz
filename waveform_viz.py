import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st

def generate_waveform(wave_type, frequency=0.0):
    t = np.linspace(0, 1, 1000)
    
    if wave_type == 'sine':
        waveform = np.sin(2 * np.pi * frequency * t)
    elif wave_type == 'square':
        waveform = signal.square(2 * np.pi * frequency * t)
    elif wave_type == 'sawtooth':
        waveform = signal.sawtooth(2*np.pi*frequency*t)
    elif wave_type == 'triangle':
        waveform = signal.sawtooth(2*np.pi*frequency*t,width=0.5) 
    else:
        waveform = np.random.normal(size=len(t))
        
    return t, waveform

st.title('Waveform Visualizer by V McCoy')

waveforms = ['sine', 'square', 'sawtooth', 'triangle', 'noise']
selected_waveform = st.selectbox('Select Waveform:', waveforms)
frequency_input_value_hz=0

if selected_waveform != 'noise':
    frequency_input_value_hz = st.slider('Frequency (Hz):', min_value=0, max_value=20000)

t_vals, y_vals = generate_waveform(selected_waveform, frequency_input_value_hz)

fig, ax = plt.subplots()
ax.plot(t_vals, y_vals)

ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')

st.pyplot(fig)
