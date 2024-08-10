# EEG Signal Simulation and Analysis

## Overview

This repository contains two Python scripts for simulating and analyzing EEG signals:

1. **`eeg_simulator.py`**: Simulates EEG signals for different physiological states and saves them to CSV files.
2. **`eeg_waves.py`**: Reads EEG data from CSV files, processes it to extract different EEG bands, and plots the results.

## Installation

1. Ensure you have Python 3.x installed.
2. Install the required libraries using pip:
   ```bash
   pip install numpy pandas matplotlib scipy

Usage
EEG Simulation
The eeg_simulator.py script generates simulated EEG signals for various states and saves them as CSV files.

Open eeg_simulator.py.
Set the desired sampling frequency (fs) and duration of the signal.
fs (Sampling frequency): Frequency at which data points are sampled (e.g., 256 Hz).
duration (Duration): Length of the signal in seconds (e.g., 10 seconds).
Run the script to generate and save simulated EEG signals for different states (wake, rem, deep_sleep, light_sleep).
The simulated data will be saved as CSV files in the same directory with names like wake_eeg.csv, rem_eeg.csv, etc.
Optionally, you can visualize the raw EEG signal using the plot function provided in the script.

EEG Analysis
The eeg_waves.py script reads EEG data from CSV files, filters it into different frequency bands, and plots the results.
Open eeg_waves.py.
Update the base_directory variable to the path where your CSV files are located.
Set base_directory to the folder path containing your CSV files (e.g., r'C:\Users\YourName\Desktop\Python Projects\EEG_analysis').
Set the filename variable to the name of the CSV file you want to analyze.
Example: filename = 'wake_eeg.csv'.
Run the script to load the data, filter it into different EEG bands (Delta, Theta, Alpha, Beta), and generate plots.
The resulting plots will show the amplitude of different EEG frequency bands over time.

Notes
The eeg_simulator.py script is optional and intended for testing purposes in the absence of real EEG data.
Ensure that the base_directory in eeg_waves.py is correctly set to the directory where your CSV files are stored.
Adjust the filename in eeg_waves.py to match the CSV file you wish to analyze.

License
This project is licensed under the MIT License. See the LICENSE file for details.


### Key Sections:
- **Overview**: Briefly describes what each script does.
- **Installation**: Instructions to set up the Python environment and install dependencies.
- **Usage**: Detailed steps on how to use each script, including setting parameters and running the scripts.
- **Notes**: Additional information on optional usage and directory settings.
- **License**: Licensing information.
