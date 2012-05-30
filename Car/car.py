from __future__ import division
from visual.graph import *
t=0
theta = 1e-3
time_int = 0.1
time_int_int = int(time_int/theta)
scene.autoscale = 1
scene.center = (2.1,0,0)
messagebox = label(pos=(2.1,-1,0))

#Graph of position
graphP = gdisplay(x=450, y=0, title="Position vs Time Graph", width=600, height=400, xtitle="Time (s)", ytitle="Position (m)")
carP = gcurve(gdisplay=graphP, color=color.red)

#Graph of velocity
graphV = gdisplay(x=500, y=50, title="Velocity vs Time Graph", width=600, height=400, xtitle="Time (s)", ytitle="Velocity (m/s)")
carV = gcurve(gdisplay=graphV, color = color.cyan)

#Graph of acceleration
graphA = gdisplay(x=550, y=100, title="Acceleration vs Time Graph", width=600, height=400, xtitle="Time (s)", ytitle="Acceleration (m/s^2)")
carA = gcurve(gdisplay=graphA, color = color.yellow)

#Track
road = box(pos=(2.1,0,0), length=5, height=0.05, width=0.2)

#Car Properties
car = box(pos = (0,0.1,0), length=0.2, height=0.05, width=0.1, color=color.red)
wheel1 = cylinder(pos = (-0.09,0.05,0.04), axis=(0,0,0.01), radius=0.025, color=color.yellow)
wheel2 = cylinder(pos = (0.09,0.05,0.04), axis=(0,0,0.01), radius=0.025, color=color.yellow)
wheel3 = cylinder(pos = (-0.09,0.05,-0.05), axis=(0,0,0.01), radius=0.025, color=color.yellow)
wheel4 = cylinder(pos = (0.09,0.05,-0.05), axis=(0,0,0.01), radius=0.025, color=color.yellow)
car.v = vector(0,0,0)
car.a = vector(0,0,0)

#Empty lists for time values
tlist = []
vlist = []
alist = []

#Forward Movement of the Car
while t <= 8.24354:
    rate(500)
    car.v = vector(0.10182*t,0,0)
    car.a = vector(0.10182,0,0)
    car.pos = vector(((0.05091*(t**2))+(0.06555*t)),0.1,0)
    wheel1.pos = vector(-0.09+((0.05091*(t**2))+(0.06555*t)),0.05,0.04)
    wheel2.pos = vector(0.09+((0.05091*(t**2))+(0.06555*t)),0.05,0.04)
    wheel3.pos = vector(-0.09+((0.05091*(t**2))+(0.06555*t)),0.05,-0.05)
    wheel4.pos = vector(0.09+((0.05091*(t**2))+(0.06555*t)),0.05,-0.05)

    carP.plot(pos=(t,car.pos.x))
    carV.plot(pos=(t,car.v.x))
    carA.plot(pos=(t,car.a.x))
    
    tlist.append(t)
    vlist.append(car.v.x) 
    alist.append(car.a.x)    
    t = t + theta

    #Message Box
    message = "Position of the Car: " + str(car.pos)
    message += "\nVelocity of the Car: " + str(car.v)
    message += "\nAcceleration of the Car: " + str(car.a)
    messagebox.text =  message

#Backward Movement of the Car
t = 8.24354

while t <= 17.7077:
    rate(500)
    car.v = vector(-0.10732*t + 0.9699,0,0)
    car.a = vector(-0.10732,0,0)
    car.pos = vector(-0.05366*(t**2) + 0.9699*t - 0.348893,0.1,0)
    wheel1.pos = vector(-0.09-0.05366*(t**2) + 0.9699*t - 0.348893,0.05,0.04)
    wheel2.pos = vector(0.09-0.05366*(t**2) + 0.9699*t - 0.348893,0.05,0.04)
    wheel3.pos = vector(-0.09-0.05366*(t**2) + 0.9699*t - 0.348893,0.05,-0.05)
    wheel4.pos = vector(0.09-0.05366*(t**2) + 0.9699*t - 0.348893,0.05,-0.05)

    carP.plot(pos=(t,car.pos.x))
    carV.plot(pos=(t,car.v.x))
    carA.plot(pos=(t,car.a.x))
    
    tlist.append(t)
    vlist.append(car.v.x) 
    alist.append(car.a.x)    
    t = t + theta

    #Message Box
    message = "Position of the Car: " + str(car.pos)
    message += "\nVelocity of the Car: " + str(car.v)
    message += "\nAcceleration of the Car: " + str(car.a)
    messagebox.text =  message
