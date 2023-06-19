import numpy as np
import matplotlib.pyplot as plt
from pykalman import KalmanFilter

# Generate a noisy sinusoidal signal
np.random.seed(0)
N = 200  # Number of data points
t = np.arange(N)
x = np.linspace(0, 2 * np.pi, N)
true_signal = np.sin(x)  # True sinusoidal signal
noise = np.random.normal(0, 0.4, N)  # Gaussian noise
observed_signal = true_signal + noise  # Observed signal with noise

# Define the Kalman filter model
transition_matrix = np.array([[1, 1], [0, 1]])  # State transition matrix
observation_matrix = np.array([[1, 0]])  # Observation matrix
initial_state_mean = np.array([observed_signal[0], 0])  # Initial state mean
initial_state_covariance = np.eye(2)  # Initial state covariance
observation_covariance = 1 ** 2  # Observation noise covariance (increase for more smoothing)
transition_covariance = np.array([[0.01 ** 2, 0], [0, 0.01 ** 2]])  # Transition noise covariance (increase for more smoothing)

# Create a Kalman filter
kf = KalmanFilter(
    transition_matrices=transition_matrix,
    observation_matrices=observation_matrix,
    initial_state_mean=initial_state_mean,
    initial_state_covariance=initial_state_covariance,
    observation_covariance=observation_covariance,
    transition_covariance=transition_covariance
)

# Perform filtering
filtered_state_means, filtered_state_covariances = kf.filter(observed_signal)

# Extract filtered signal from the state means
filtered_signal = filtered_state_means[:, 0]

# Plot the original signal, observed signal, and filtered signal
plt.figure(figsize=(10, 6))
plt.plot(t, true_signal, linestyle='--', label='Sinusoid')
plt.plot(t, observed_signal, label='Messsignal')
plt.plot(t, filtered_signal, label='Kalman-Schätzung')
plt.xticks(np.arange(min(t), max(t)+20, 20))
plt.xlabel('Zeit')
plt.ylabel('Wert')
plt.title('Kalman Filterung des sinusförmiges Signals')
plt.grid(True)
plt.legend()
plt.show()


