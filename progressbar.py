### Author: Lars Weiler
### Description: progress bar
### Category: fun
### License: THE NERD-WARE LICENSE (Revision 2)
### Appname: progressbar

import pyb
import ugfx

ugfx.init()
h = ugfx.height()
w = ugfx.width()

ugfx.clear(ugfx.BLACK)

lw = 240    # progress bar width
lh = 40     # progress bar height
m = 5       # margin
s = 1       # step

ugfx.box((w//2)-(lw//2), (h//2)-(lh//2), lw, lh, ugfx.WHITE)
for i in range(m, lw-2*m, s):
    # use the 30bit random number, bitshift by 24 bits, which will give 0-65
    # and use this number for the delay in milliseconds
    pyb.delay(pyb.rng()>>24)
    ugfx.area((w//2)-(lw//2-m), (h//2)-(lh//2-m), i, (lh-2*m), ugfx.WHITE)
# wait 500ms and blank the screen
pyb.delay(500)
ugfx.clear(ugfx.BLACK)

