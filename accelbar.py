### Author: Lars Weiler
### Description: accelerators to progress bars
### Category: fun
### License: THE NERD-WARE LICENSE (Revision 2)
### Appname: accelbar

from imu import IMU
import pyb
import ugfx
import buttons

imu = IMU()

buttons.init()

ugfx.init()
h = ugfx.height()
w = ugfx.width()

bgcolor = ugfx.BLACK    # foreground colour
fgcolor = ugfx.WHITE    # background colour

ugfx.clear(bgcolor)

pw = 40     # progress bar width
ph = h - 20 # progress bar height
pm = 5      # progress bar margin

# draw the boxes for the progress bars
ugfx.box((w//2)-(w//4)-(pw//2), (h//2)-(ph//2), pw, ph, fgcolor)
ugfx.box((w//2)-(pw//2), (h//2)-(ph//2), pw, ph, fgcolor)
ugfx.box((w//2)+(w//4)-(pw//2), (h//2)-(ph//2), pw, ph, fgcolor)

# label the progress bars
ugfx.text((w//2)-(w//4)-(pw//2)-15, (h//2), 'x', fgcolor)
ugfx.text((w//2)-(pw//2)-15,        (h//2), 'y', fgcolor)
ugfx.text((w//2)+(w//4)-(pw//2)-15, (h//2), 'z', fgcolor)

while not buttons.is_pressed("BTN_MENU"):
    accel = imu.get_acceleration()
    accel_x = accel.get('x')
    accel_y = accel.get('y')
    accel_z = accel.get('z')

    # if acceleration exceeds abs(1), paint the progress bar red
    if accel_x > 1:
        accel_x = 1
        fgcolor_x = ugfx.RED
    elif accel_x < -1:
        accel_x = -1
        fgcolor_x = ugfx.RED
    else:
        fgcolor_x = ugfx.WHITE

    if accel_y > 1:
        accel_y = 1
        fgcolor_y = ugfx.RED
    elif accel_y < -1:
        accel_y = -1
        fgcolor_y = ugfx.RED
    else:
        fgcolor_y = ugfx.WHITE

    if accel_z > 1:
        accel_z = 1
        fgcolor_z = ugfx.RED
    elif accel_z < -1:
        accel_z = -1
        fgcolor_z = ugfx.RED
    else:
        fgcolor_z = ugfx.WHITE

    # paint progress bar for x
    if accel_x >= 0:
        ugfx.area(
                (w//2)-(w//4)-(pw//2-pm),
                (h//2),
                (pw-2*pm),
                int((ph//2-2*pm)*accel_x),
                fgcolor_x)
    else:
        ugfx.area(
                (w//2)-(w//4)-(pw//2-pm),
                (h//2+int((ph//2-2*pm)*accel_x)),
                (pw-2*pm),
                (abs(int((ph//2-2*pm)*accel_x))),
                fgcolor_x)

    # paint progress bar for y
    if accel_y >= 0:
        ugfx.area(
                (w//2)-(pw//2-pm),
                (h//2),
                (pw-2*pm),
                int((ph//2-2*pm)*accel_y),
                fgcolor_y)
    else:
        ugfx.area(
                (w//2)-(pw//2-pm),
                (h//2+int((ph//2-2*pm)*accel_y)),
                (pw-2*pm),
                (abs(int((ph//2-2*pm)*accel_y))),
                fgcolor_y)

    # paint progress bar for z
    if accel_z >= 0:
        ugfx.area(
                (w//2)+(w//4)-(pw//2-pm),
                (h//2),
                (pw-2*pm),
                int((ph//2-2*pm)*accel_z),
                fgcolor_z)
    else:
        ugfx.area(
                (w//2)+(w//4)-(pw//2-pm),
                (h//2+int((ph//2-2*pm)*accel_z)),
                (pw-2*pm),
                (abs(int((ph//2-2*pm)*accel_z))),
                fgcolor_z)

    pyb.delay(100)

    # repaint filled area with bgcolor
    # x
    ugfx.area(
            (w//2)-(w//4)-(pw//2-pm),
            (h//2)-(ph//2-pm),
            (pw-2*pm),
            ph-2*pm,
            bgcolor)
    # y
    ugfx.area(
            (w//2)-(pw//2-pm),
            (h//2)-(ph//2-pm),
            (pw-2*pm),
            ph-2*pm,
            bgcolor)
    # z
    ugfx.area(
            (w//2)+(w//4)-(pw//2-pm),
            (h//2)-(ph//2-pm),
            (pw-2*pm),
            ph-2*pm,
            bgcolor)

ugfx.clear(bgcolor)
