import cv2
import sys

def handle_input():
    global threshold
    global setting

    key = cv2.waitKey(50)
    if key == ord('1'):
        setting = 1
    if key == ord('2'):
        setting = 2
    if key == ord('3'):
        setting = 3
    if key == ord('w'):
        threshold += 1
        update_intensity_map()
    if key == ord('s'):
        threshold = max(threshold-1, 0)
        update_intensity_map()
    return key

def update_intensity_map():
    global intensity_map
    intensity_map = intensity_map_def
    for i in range(threshold):
        intensity_map += ' '


# -- Settings --

# Settings 1: Close View 90 -> 50, 50
# Settings 2: Wide View: 150 -> 50, 50
# Settings 3: Fullscreen 2000 -> 70, 50
setting = 2
threshold = 17
intensity_map = ''

last_face_threshold = 80
last_face_x = None
last_face_y = None

# intensity_map_def = '▓Ñ▒@#W░$9876543210?!abc;:+=-,._'
# intensity_map_def = '▒Ñ@BW░#032|1:_-,.'
intensity_map_def = '▓Ñ▒@W░321:-,.'

update_intensity_map()



# -- Start --
vid = cv2.VideoCapture(int(sys.argv[1]))
detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

while vid.isOpened():
    ret, frame = vid.read()
    if ret == False:
        break

    faces = detector.detectMultiScale(frame)
    
    if len(faces) < 1 and setting != 3:
        continue
    
    img_height, img_width, channels = frame.shape
    
    if setting == 3:
        r = 2000
        m_x = img_width / 2
        m_y = img_height / 2
    else:
        face = faces[0]
        (x,y,w,d) = face

        if setting == 1:
            r = 90
        elif setting == 2:
            r = 150
        
        m_x = int((x + x + w) / 2)
        m_y = int((y + y + d) / 2)
        if last_face_x == None:
            last_face_x = m_x
            last_face_y = m_y
        
        delta = abs(last_face_x - m_x) + abs(last_face_y - m_y)
        if delta > last_face_threshold:
            cv2.imshow('frame', final_frame)
            key = handle_input()
            if key == ord('q'):
                break
            if key != 13: # Enter
                continue # Face is too far away this frame, ignore
        
        last_face_x = m_x
        last_face_y = m_y

    r_start = max(0, m_y-r)
    r_end = min(img_height, m_y+r)
    c_start = max(0, m_x-r)
    c_end = min(img_width, m_x+r)
    frame = frame[r_start:r_end, c_start:c_end]
    
    if setting == 3:
        dw = 70
        dh = 50
    else:
        dw = 50
        dh = 50

    frame = cv2.resize(frame, (dw, dh), interpolation=cv2.INTER_AREA)
    final_frame = frame
    cv2.imshow('frame', frame)
    img_height, img_width, channels = frame.shape

    max_int = 0
    min_int = 1
    for i in range(img_height):
        for j in range(img_width):
            k = frame[i,j]
            avg = (int(k[0]) + int(k[1]) + k[2]) / (3.0 * 255)
            max_int = max(max_int, avg)
            min_int = min(min_int, avg)

    msg = ''

    for i in range(img_height):
        for j in range(img_width):
            k = frame[i,j]
            avg = (int(k[0]) + int(k[1]) + int(k[2])) / (3.0 * 255)
            avg = (avg - min_int) / (max_int - min_int)
            val = max(0, len(intensity_map) - int(avg * len(intensity_map)) - 1)
            msg += intensity_map[val] + intensity_map[val]
        msg += '\n'
    print(msg)

    key = handle_input()
    if key == ord('q'):
        break