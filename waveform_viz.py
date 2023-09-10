import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st
from scipy.io.wavfile import write
import os
from IPython.lib.display import Audio

SAMPLE_RATE = 44100
DURATION = 10

def generate_waveform_stretched(wave_type, frequency=0.0, sample_rate=SAMPLE_RATE, duration=DURATION):
    t = np.linspace(0, duration, sample_rate * duration, False)
    
    if wave_type == 'sine':
        waveform = 0.5 * np.sin(2 * np.pi * frequency * t)
    elif wave_type == 'square':
        waveform = 0.5 * signal.square(2 * np.pi * frequency * t)
    elif wave_type == 'sawtooth':
        waveform = 0.5 * signal.sawtooth(2*np.pi*frequency*t)
    elif wave_type == 'triangle':
        waveform = 0.5 * signal.sawtooth(2*np.pi*frequency*t,width=0.5) 
    else:
        waveform = np.random.normal(size=len(t))

    return t, waveform

st.title('Waveform Visualizer by V McCoy')

waveforms = ['sine', 'square', 'sawtooth', 'triangle', 'noise']
selected_waveform = st.selectbox('Select Waveform:', waveforms)
frequency_input_value_hz=0

if selected_waveform != 'noise':
    frequency_input_value_hz = st.slider('Frequency (Hz):', min_value=0, max_value=20000)

t_vals, y_vals = generate_waveform_stretched(selected_waveform, frequency_input_value_hz)

fig, ax = plt.subplots()
ax.plot(t_vals[:1000], y_vals[:1000])  # plot only first 1000 samples
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')

st.pyplot(fig)

if st.button('Generate and play sound'):
    filename = 'out.wav'
    scaled = np.int16(y_vals/np.max(np.abs(y_vals)) * 32767)
    write(filename, SAMPLE_RATE, scaled)

    st.audio(Audio(filename, autoplay=True))
