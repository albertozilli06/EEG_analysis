import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def generate_wave(frequency, amplitude, fs, duration):
    """
    Generate a sine wave with a specific frequency and amplitude.

    Parameters:
    - frequency: Frequency of the sine wave (Hz)
    - amplitude: Amplitude of the sine wave
    - fs: Sampling frequency (Hz)
    - duration: Duration of the signal (seconds)

    Returns:
    - wave: Generated sine wave
    """
    t = np.arange(0, duration, 1/fs)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave

def simulate_eeg_state(fs, duration, state):
    """
    Simulate EEG signals for different physiological states.

    Parameters:
    - fs: Sampling frequency (Hz)
    - duration: Duration of the signal (seconds)
    - state: Physiological state ('wake', 'rem', 'deep_sleep', 'light_sleep')

    Returns:
    - eeg_signal: Simulated EEG signal
    """
    time = np.arange(0, duration, 1/fs)
    eeg_signal = np.zeros(len(time))
    
    if state == 'wake':
        # Wake state: Dominated by alpha and beta waves
        eeg_signal += generate_wave(10, 0.5, fs, duration)  # Alpha
        eeg_signal += generate_wave(20, 0.3, fs, duration)  # Beta
        
    elif state == 'rem':
        # REM sleep: Dominated by theta waves, with some alpha
        eeg_signal += generate_wave(6, 0.5, fs, duration)   # Theta
        eeg_signal += generate_wave(10, 0.2, fs, duration)  # Alpha
        
    elif state == 'deep_sleep':
        # Deep sleep: Dominated by delta waves
        eeg_signal += generate_wave(2, 0.6, fs, duration)   # Delta
        eeg_signal += generate_wave(4, 0.2, fs, duration)   # Theta
        
    elif state == 'light_sleep':
        # Light sleep: Dominated by theta waves
        eeg_signal += generate_wave(6, 0.5, fs, duration)   # Theta
        eeg_signal += generate_wave(10, 0.1, fs, duration)  # Alpha
        
    else:
        raise ValueError("Unknown state. Choose from 'wake', 'rem', 'deep_sleep', or 'light_sleep'.")
    
    # Add some random noise
    noise = np.random.normal(0, 0.05, len(time))
    eeg_signal += noise
    
    return eeg_signal

def save_eeg_to_csv(eeg_signal, fs, filename):
    """
    Save EEG signal data to a CSV file.

    Parameters:
    - eeg_signal: EEG signal data
    - fs: Sampling frequency (Hz)
    - filename: Name of the CSV file to save
    """
    time = np.arange(0, len(eeg_signal)) / fs
    data = {
        'Time': time,
        'EEG': eeg_signal
    }
    df = pd.DataFrame(data)
    
    # Save to the same directory where the script is run
    filepath = os.path.join(os.getcwd(), filename)
    df.to_csv(filepath, index=False)
    print(f"EEG data saved to {filepath}")

def plot_raw_eeg(eeg_signal, fs, title):
    """
    Plot the raw EEG signal for reference.

    Parameters:
    - eeg_signal: EEG signal data
    - fs: Sampling frequency (Hz)
    - title: Title of the plot
    """
    time = np.arange(0, len(eeg_signal)) / fs
    plt.figure(figsize=(10, 4))
    plt.plot(time, eeg_signal)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

# Main script settings
fs = 256  # Sampling frequency in Hz
duration = 10  # Duration of the signal in seconds

# Simulate and save EEG for different states
states = ['wake', 'rem', 'deep_sleep', 'light_sleep']
for state in states:
    eeg_signal = simulate_eeg_state(fs, duration, state)
    filename = f'{state}_eeg.csv'
    save_eeg_to_csv(eeg_signal, fs, filename)
    plot_raw_eeg(eeg_signal, fs, f'{state.capitalize()} EEG')
