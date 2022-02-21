import cv2
import sys

# Open webcam with the index passed as an argument
vid = cv2.VideoCapture(int(sys.argv[1]))

# Flag for whether we have captured the isolated background
bg_set = False

while vid.isOpened():
    ret, frame = vid.read()
    if ret == False:
        break # Exit if we couldn't read from the camera
    
    cv2.imshow('frame', frame)

    if bg_set:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(frame_gray, bg_gray)
        # th, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        cv2.imshow('diff', diff)
    
    key = cv2.waitKey(16)
    if key == ord('q'):
        break
    if key == 13: #enter
        bg_set = True
        bg = frame
        bg_gray = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

vid.release()
cv2.destroyAllWindows()