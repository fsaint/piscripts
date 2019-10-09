from time import sleep
from picamera import PiCamera

from send import alert 

import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


camera = PiCamera()
camera.resolution = (1024, 768)
#camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')


alert("Doctest",title=f"IP: {get_ip_address()}", sound="magic",attachment=open("foo.jpg","rb"),url_title="School 4 One Link")
