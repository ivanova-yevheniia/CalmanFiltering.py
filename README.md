# Kalman Filter
GPS-data processing using Calman Filter

1. Download all required libraries:  **pip install -r requirements.txt**
2. Example of Kalman Filtering with Sinusoidal Signal **python testCalman.py**.
Results:  **start report/sin.png**
3. Get your GPS-data with app [GPS Logger](https://play.google.com/store/apps/details?id=eu.basicairdata.graziano.gpslogger&hl=de)
4. Import your data with extension gpx to **data** folder
5. Paste in **parsep.py** to variable **dt** the path to your file
6. Run the code **python calman_GPS.py**
7. All data before and after filtering were saved in data folder **measurements.csv** and **calman.csv**
8. Upload both files in [GPSVisualizer](https://www.gpsvisualizer.com/map_input?form=data) choose map parameters
for plotting results on the map.
9. Results: **start report/plot.png**, maps: 
**start report/before.png**  and 
**start report/filter.png**
