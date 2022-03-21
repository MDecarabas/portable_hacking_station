from djitellopy import Tello

tello = Tello() # connect to tello drone

tello.connect() # connect to tello drone socket
tello.takeoff() # take off with the drone

# small movement
tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

tello.land() #tello land