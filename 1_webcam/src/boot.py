import config
import network
import utime
import machine
import camera

camera.init(0, format=camera.JPEG,framesize=camera.FRAME_QVGA, xclk_freq=camera.XCLK_20MHz )
# camera.init(0, format=camera.GRAYSCALE,framesize=camera.FRAME_QVGA, xclk_freq=camera.XCLK_20MHz )
pin = machine.Pin(14, machine.Pin.OUT)

sta_if = network.WLAN(network.STA_IF)
start_ms = utime.ticks_ms()

if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(config.WIFI_SSID, config.WIFI_PASS)
    while True:        
        if sta_if.isconnected():
            break
        if utime.ticks_ms() - start_ms >= 20000:
            break
        utime.sleep_ms(100)

if sta_if.isconnected():
    print('network config:', sta_if.ifconfig())
    pin.off()
else: 
    print('internet not available')

