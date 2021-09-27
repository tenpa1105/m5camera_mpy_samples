import uasyncio
import image
import picoweb
import ure as re
import gc
import camera

face_cascade = image.HaarCascade("frontalface", stages=25)

def index(req, resp):
    yield from app.sendfile(resp, "html/index.html")

def camera_streaming(req, resp):
    try:
        frame_count = 0
        while True:
            if frame_count == 0:
                yield from picoweb.start_response(resp, "multipart/x-mixed-replace; boundary=myboundary")


            img =camera.capture()
            if img == False:
                await uasyncio.sleep(0.1)
                print("capture error")
                continue

            if img.format() != 5: #not jpeg
                objects = img.find_features(face_cascade, threshold=0.75, scale_factor=1.25)
                for r in objects:
                    img.draw_rectangle(r, fill=False)
                img.compress(30)

            yield from resp.awrite('--myboundary\r\n')
            yield from resp.awrite("Content-Type: image/jpeg\r\nContent-Length: " + str(img.size()) + "\r\n\r\n")
            yield from resp.awrite(img.to_bytes())
            frame_count += 1
    except OSError:
        print("camera error")
        yield from resp.aclose()

ROUTES = [#
    ("/", index),
    (re.compile('^/camera/'), camera_streaming),
]

import ulogging as logging
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

gc.collect()
app = picoweb.WebApp(__name__, ROUTES)
app.run(host='192.168.0.90',debug=-1)