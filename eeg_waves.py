import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import os

# Set the base directory for file paths
# Replace 'Replace with your folder' with the path to the directory where your CSV files are located.
base_directory = r'Replace with your folder'  # Use raw string literal or forward slashes

def butter_bandpass(lowcut, highcut, fs, order=4):
    """
    Design a bandpass filter.

    Parameters:
    - lowcut: Lower cutoff frequency (Hz)
    - highcut: Higher cutoff frequency (Hz)
    - fs: Sampling frequency (Hz)
    - order: Filter order (default is 4)

    Returns:
    - b: Numerator polynomial of the filter
    - a: Denominator polynomial of the filter
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    """
    Apply a bandpass filter to data.

    Parameters:
    - data: Input signal data
    - lowcut: Lower cutoff frequency (Hz)
    - highcut: Higher cutoff frequency (Hz)
    - fs: Sampling frequency (Hz)
    - order: Filter order (default is 4)

    Returns:
    - y: Filtered signal
    """
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

def filter_eeg_signal(eeg_data, fs):
    """
    Filter EEG data into different frequency bands.

    Parameters:
    - eeg_data: Raw EEG signal data
    - fs: Sampling frequency (Hz)

    Returns:
    - delta: Delta band signal
    - theta: Theta band signal
    - alpha: Alpha band signal
    - beta: Beta band signal
    """
    delta = bandpass_filter(eeg_data, 0.5, 4, fs)
    theta = bandpass_filter(eeg_data, 4, 8, fs)
    alpha = bandpass_filter(eeg_data, 8, 13, fs)
    beta = bandpass_filter(eeg_data, 13, 30, fs)
    return delta, theta, alpha, beta

def plot_eeg_bands(delta, theta, alpha, beta, fs, filename):
    """
    Plot the EEG data for different frequency bands.

    Parameters:
    - delta: Delta band signal
    - theta: Theta band signal
    - alpha: Alpha band signal
    - beta: Beta band signal
    - fs: Sampling frequency (Hz)
    - filename: Name of the file being analyzed (used in plot title)
    """
    time = np.arange(len(delta)) / fs

    plt.figure(figsize=(12, 8))
    plt.suptitle(f'EEG Bands for {filename}', fontsize=16)  # Title for the whole plot

    plt.subplot(4, 1, 1)
    plt.plot(time, delta, color='blue')
    plt.title('Delta Band (0.5 - 4 Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(4, 1, 2)
    plt.plot(time, theta, color='green')
    plt.title('Theta Band (4 - 8 Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(4, 1, 3)
    plt.plot(time, alpha, color='red')
    plt.title('Alpha Band (8 - 13 Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(4, 1, 4)
    plt.plot(time, beta, color='purple')
    plt.title('Beta Band (13 - 30 Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to fit suptitle
    plt.show()

def load_eeg_data(filename):
    """
    Load EEG data from a CSV file.

    Parameters:
    - filename: Name of the CSV file

    Returns:
    - eeg_data: Raw EEG signal data
    """
    filepath = os.path.join(base_directory, filename)
    return pd.read_csv(filepath)['EEG'].values

def eeg_analysis_pipeline(filename, fs):
    """
    Load EEG data, filter it into different bands, and plot the results.

    Parameters:
    - filename: Name of the CSV file
    - fs: Sampling frequency (Hz)
    """
    # Load EEG data
    eeg_data = load_eeg_data(filename)
    
    # Filter the EEG data into different frequency bands
    delta, theta, alpha, beta = filter_eeg_signal(eeg_data, fs)
    
    # Plot the filtered EEG bands with the filename in the title
    plot_eeg_bands(delta, theta, alpha, beta, fs, filename)

# Example usage
# Set the filename and sampling frequency
filename = 'your_file.csv'  # Change this to the filename you want to analyze
fs = 256  # Sampling frequency in Hz

# Analyze the EEG data
eeg_analysis_pipeline(filename, fs)
