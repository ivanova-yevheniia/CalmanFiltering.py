import numpy as np
import matplotlib.pyplot as plt
from pykalman import KalmanFilter
from parser import dt as f
import pandas as pd

f=f.head(50)
print(f['lon'].min(), f['lon'].max(),
         f['lat'].min(), f['lat'].max())

N = len(f)
measurements = np.zeros(N*2).reshape(N, 2)
for row in range(0, len(f)):
    measurements[row][0] = f.iloc[row]['lon']
    measurements[row][1] = f.iloc[row]['lat']

df = pd.DataFrame(columns=['lon', 'lat'])
for row in range(0, N):
    df.loc[len(df)] = [measurements[row][0], measurements[row][1]]
filename = 'data/measurements.csv'
df.to_csv(filename, index=False)

initial_state_mean = [measurements[0, 0], 0, measurements[0, 1], 0]

transition_matrix = [[1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 1],
                     [0, 0, 0, 1]]

observation_matrix = [[1, 0, 0, 0],
                      [0, 0, 1, 0]]

kf1 = KalmanFilter(transition_matrices=transition_matrix,
                  observation_matrices=observation_matrix,
                  initial_state_mean=initial_state_mean)

kf1 = kf1.em(measurements, n_iter=100)
(smoothed_state_means, smoothed_state_covariances) = kf1.smooth(measurements)

plt.figure(1)
plt.plot(measurements[:, 0], measurements[:, 1], 'bo', label='Messignal')
plt.plot(smoothed_state_means[:, 0], smoothed_state_means[:, 2], 'r--', label='Kalman-Schätzung')


new_df = pd.DataFrame(columns=['lon', 'lat'])
for row in range(0, len(smoothed_state_means)):
    new_df.loc[len(new_df)] = [smoothed_state_means[row, 0], smoothed_state_means[row, 2]]
filename = 'data/calman.csv'
new_df.to_csv(filename, index=False)


'''Plot on the map for long distance'''
#ruh_m = plt.imread('data/map.png')
#fig, ax = plt.subplots()
#ax.set_xlim(BBox[0], BBox[1])
#ax.set_ylim(BBox[2], BBox[3])
#ax.scatter(f['lon'], f['lat'], zorder=1, alpha=0.2, c='b', s=10)
#plt.plot(smoothed_state_means[:, 0], smoothed_state_means[:, 2], 'r--')
#ax.imshow(ruh_m, zorder=0, extent=BBox, aspect='equal')

plt.legend(loc='lower right', bbox_to_anchor=(1, 0))
plt.show()
