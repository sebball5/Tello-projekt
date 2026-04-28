from djitellopy import Tello
import time

tello = Tello()

tello.connect()
print("Battery:", tello.get_battery())

tello.takeoff()

time.sleep(2)

tello.move_up(50)   # move up 50 cm
time.sleep(2)

tello.land()