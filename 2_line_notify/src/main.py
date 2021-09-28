import gc
import camera
import urequests
import utime
import config

LINE_TOKEN = config.LINE_TOKEN 
LINE_URL = "https://notify-api.line.me/api/notify"

def make_line_request(data, image=None):
    boundary = '----boudary' 
    body = b''
    body += b'--%s\r\n' % boundary
    body += b'Content-Disposition: form-data; name="message"\r\n\r\n' 
    body += b'%s\r\n' % data
    body += b'--%s\r\n' % boundary
    body += b'Content-Disposition: form-data; name="imageFile"; filename="latest.jpeg"\r\n'
    body += b'Content-Type : image/jpeg\r\n\r\n'
    body += bytes(image)
    body += b'\r\n'
    body += b'--%s--\r\n' % boundary
    headers = {
        'User-Agent': 'mpy',
        'Accept': '*/*',
        'Authorization': 'Bearer ' + LINE_TOKEN,
        'Content-Type': 'multipart/form-data; boundary=' + boundary,
        }
    return body, headers


def send_line(message, img):
    body,headers = make_line_request( message, bytes(img))
    r = urequests.post(LINE_URL, data=body, headers=headers).json()
    print(r)

while True:
    bg_img = camera.capture()
    utime.sleep(1)

    diff = config.MOVING_DET_DIFF 
    while(diff):
        img = camera.capture()
        post_img = img.copy()
        img.difference(bg_img)
        stats = img.statistics()
        print(stats[5])
        if (stats[5] > config.MOVING_DET_LIGHT_MAX):
            diff -= 1
    post_img.compress(40)
    send_line("moving detection", post_img.to_bytes())