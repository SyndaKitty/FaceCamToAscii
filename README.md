# FaceCamToAscii
Converts webcam video to an ASCII representation.
Uses OpenCV to track a face and keep it centered

Must have OpenCV installed to run

Usage:
```python
python face_cam.py 0
```
The final parameter is the index of the camera, use 0 if you only have one video device

Press any of the following keys while focused on the small window to change the settings
- 1/2/3: Change the zoom level. 1 is closest to the face, 3 is the entire webcam view
- W/S: Change the threshold level. The higher it is, the more likely it is for dark areas to be rounded to black

Right now the output is directly to the terminal. 
I plan to have the output sent through a network socket for other uses (render out for Twitch stream?)
