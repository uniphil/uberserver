import xbmcaddon
import xbmc
import xbmcgui
import serial

addon = xbmcaddon.Addon(id='addon.gpio')
name = addon.getAddonInfo('name')

class MyPlayer(xbmc.Player):
    def __init__(self, *args, **kwargs):
        super(MyPlayer, self).__init__(*args, **kwargs)
        self.serial = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
        self.serial.write('s0.c0,0,0.')
    
    def gpio_play(self):
        self.serial.write('s1.c128,0,0.')

    def gpio_stop(self):
        self.serial.write('s0.c128,255,255')

    def gpio_pause(self):
        self.serial.write('c0,255,0')
    
    def onPlayBackStarted(self):
        xbmc.log('GPIO: start event')
        self.gpio_play()
 
    def onPlayBackPaused(self):
        xbmc.log('GPIO: pause event')
        self.gpio_pause()

    def onPlayBackResumed(self):
        xbmc.log('GPIO: resume event')
        self.gpio_play()
    
    def onPlayBackEnded(self):
        xbmc.log('GPIO: end event')
        self.gpio_stop()

    def onPlayBackStopped(self):
        xbmc.log('GPIO: stop event')
        self.gpio_stop()

player = MyPlayer()


while True:
   xbmc.sleep(30 * 60 * 1000)  # keep it alive every 1/2 hour?
xbmcgui.Dialog().ok(name, 'gpio controls off?')

xbmc.log('gpio ended.')
