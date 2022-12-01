from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.rotation = 180
camera.capture('/home/pi/Desktop/image_3.jpg')
camera.stop_preview()
