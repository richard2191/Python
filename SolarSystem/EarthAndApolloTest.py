from __future__ import division
from visual import *

G=6.67e-11 # Gravitational Constant
dt=10 # time interval

scene = display(title = 'Earth, Apollo 13, and Moon', width = 800, height = 600, background=(0,0,0))

# Declaration of Variables

# Earth
earth=sphere(pos=(0,0,0), material=materials.earth)
earth.mass=5.97e24
earth.radius=6378.5e3
earth.trail=curve(pos=earth.pos, color=color.red)

# Apollo
apollo=sphere(pos=(6551e3,0,0), material=materials.marble, color=color.blue)
apollo.velocity=vector(0,0,7801)
apollo.radius=100e3
apollo.trail=curve(pos=apollo.pos, color=apollo.color)

# Apollo Movement around the Earth
while (1==1):
    rate(250)

    # Earth Updated Position Calculation
    earth.velocity=vector(0,1000,0)
    earth.pos=earth.pos+earth.velocity*dt
    earth.trail.append(pos=earth.pos)

    # Apollo Acceleration
    R12=mag(earth.pos-apollo.pos)
    direction12=norm(earth.pos-apollo.pos)
    apollo.acceleration=(G*earth.mass/R12**2)*direction12

    # Apollo Updated Position Calculation
    apollo.velocity=apollo.velocity+apollo.acceleration*dt
    apollo.pos=apollo.pos+apollo.velocity*dt
    apollo.trail.append(pos=apollo.pos)

