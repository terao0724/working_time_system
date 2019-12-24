import cv2
import os
import datetime

def save_frame_camera_cycle(device_num, dir_path, basename, cycle, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) 
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:
        ret, frame = cap.read()
        img = cv2.rectangle(frame, (100,10), (550,460), (255,0,0), thickness=5)
        cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
        if n == cycle:
            n = 0
            dst = frame[10:460,100:550]
            cv2.imwrite('{}_{}.{}'.format(base_path, datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'), ext), dst)
            
        n += 1

    cv2.destroyWindow(window_name)


save_frame_camera_cycle(0, './寺尾A/', 'camera_capture_cycle', 1)
