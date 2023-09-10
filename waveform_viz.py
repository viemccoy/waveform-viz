import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st
from scipy.io.wavfile import write
from io import BytesIO
import pandas as pd

SAMPLE_RATE = 44100
DURATION = 10

@st.cache
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

    return waveform

st.title('Waveform Visualizer by V <3')

waveforms = ['sine', 'square', 'sawtooth', 'triangle', 'noise']
selected_waveform = st.selectbox('Select Waveform:', waveforms)
frequency_input_value_hz=0

if selected_waveform != 'noise':
    frequency_input_value_hz = st.slider('Frequency (Hz):', min_value=0, max_value=20000)

waveform_data = generate_waveform_stretched(selected_waveform, frequency_input_value_hz)

fig, ax = plt.subplots()
ax.plot(np.linspace(0, DURATION, SAMPLE_RATE * DURATION)[:1000], waveform_data[:1000])  # plot only first 1000 samples
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')

st.pyplot(fig)

if st.button('Generate and play sound'):
    audio = np.int16(waveform_data/np.max(np.abs(waveform_data)) * 32767)
    st.audio(audio, sample_rate=SAMPLE_RATE)
