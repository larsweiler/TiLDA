from imu import IMU
import pyb
import ugfx
import buttons

imu = IMU()


ugfx.init()

bgcolor = ugfx.BLACK
fgcolor = ugfx.YELLOW

ugfx.clear(bgcolor)
ugfx.backlight(20)

buttons.init()

t4 = pyb.Timer(4, freq=100, mode=pyb.Timer.CENTER)


while not buttons.is_pressed("BTN_MENU"):
    accel = imu.get_acceleration()
    accel_x = accel.get('x')
    accel_y = accel.get('y')
    accel_z = accel.get('z')
    accel_use = accel_y
    t4.freq(700 + accel_use * 200)
    ch1 = t4.channel(1, pyb.Timer.PWM, pin=pyb.Pin("BUZZ"), pulse_width=(t4.period() + 1) // 2)
    #ugfx.text(10,10,str(accel),ugfx.GREEN)
    ugfx.fill_circle(160, 120, 45 + int(accel_use * 45), fgcolor)
    pyb.delay(100);
    ugfx.clear(bgcolor)

ugfx.clear(ugfx.BLACK)

pyb.Pin("BUZZ", pyb.Pin.OUT).low()
