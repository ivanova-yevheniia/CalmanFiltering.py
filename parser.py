import gpxpy
import os
import numpy as np
import pandas as pd

def open_file():
    path = input('Path to gpx file: ')
    if os.path.exists(path):
        return path
    else:
        print('File does not exist!')
        open_file()

'''
    lat: latitude
    lom: longitude
'''
def get_data(gpx_file_path):
    gpx_file = open(gpx_file_path, 'r')
    gpx = gpxpy.parse(gpx_file)
    column_names = ['lat', 'lon']
    df = pd.DataFrame(columns=column_names)
    track = gpx.tracks[0]
    track_segment = track.segments[0]
    for point in track_segment.points:
        df.loc[len(df)] = [point.latitude, point.longitude]
    gpx_file.close()
    return df

dt = get_data('data/Forest.gpx')

#noise = get_data("C:\\Users\\yevhe\\PycharmProjects\\calmanFilter\\data\\Noise.gpx")
#print(forest.to_string())


