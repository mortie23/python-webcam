#!/home/nixadmin/venvs/dev/bin/python
# program to capture single image from webcam in python

# importing OpenCV library
import cv2
import modules.timeminute as tm

# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
cam_port = 0
cam = cv2.VideoCapture(cam_port)

def capture:
    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    if result:
        # saving image in local storage
        imagename = f'webcam-{tm.timeminute()}'
        cv2.imwrite(f"/var/www/html/webcam/{imagename}.jpg", image)

    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

while True:
    capture()
    time.sleep(60)
