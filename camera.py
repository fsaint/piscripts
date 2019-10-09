from time import sleep
from picamera import PiCamera

from send import alert 

camera = PiCamera()
camera.resolution = (1024, 768)
#camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')


alert("Doctest",title="Title", sound="magic",attachment=open("foo.jpg","rb"),url_title="School 4 One Link")
