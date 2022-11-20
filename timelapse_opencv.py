import cv2
import time

# find camera port
def find_camera():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

camera_list = find_camera()
print(f"the working camera is: {camera_list}")

# choose your camera and setup interval
target_camera = 0
interval = 0.5

cap = cv2.VideoCapture(target_camera)

while True:
    # capture
    ret, img = cap.read()
    # save file
    timestamp = time.time()
    cv2.imwrite(f'./img_{timestamp}.png', img)
    time.sleep(interval)
