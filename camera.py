from time import sleep
from picamera import PiCamera
from PIL import Image
from send import alert 
import io
import socket
import time
from inky import InkyWHAT

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

stream = io.BytesIO()

with PiCamera() as camera:
    camera.resolution = (1024, 768)
    #camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
#camera.start_preview()
# Camera warm-up time
stream.seek(0)
image = Image.open(stream)

inkywhat = InkyWHAT('red')

inkywhat.set_image(image.resize([400,300]).convert('P'))
inkywhat.show()
imgByteArr = io.BytesIO()
image.resize([400,300]).convert('P').save(imgByteArr, format='PNG')
alert("Doctest",title=f"IP: {get_ip_address()}", sound="magic",attachment=imgByteArr.getvalue(),url_title="School 4 One Link")
