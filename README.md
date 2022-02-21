# FaceCamToAscii
Converts webcam video to an ASCII representation

Must have OpenCV installed

Usage:
```python
python face_cam.py 0
```
The final parameter is the index of the camera, use 0 if you only have one video device

Right now the output is directly to the terminal. I plan to have the output sent through a network socket for other uses (render out for Twitch stream?)
