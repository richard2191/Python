from __future__ import division
from visual.graph import *
from visual.controls import*

#Solar System constants
G=6.67e-11
dt=.1
au=149.598e9
T = 5040 #period for going around the earth
vescape = 10905
theta = 0
deltav=1
transfer=False

##########
# Graphs #
##########

#Distance from Earth
graphPos1 = gdisplay(x=0, y=0, title="Distance from Earth vs Time Graph", width=600, height=380, xtitle="Time (s)", ytitle="Distance from Earth (m)")
mslPos1 = gcurve(gdisplay=graphPos1, color=color.cyan)

#Distance from Mars
graphPos2 = gdisplay(x=600, y=0, title="Distance from Mars vs Time Graph", width=600, height=380, xtitle="Time (s)", ytitle="Distance from Mars (m)")
mslPos2 = gcurve(gdisplay=graphPos2, color=color.cyan)

#Velocity
graphVel = gdisplay(x=0, y=380, title="MSL Velocity vs Time Graph", width=600, height=380, xtitle="Time (s)", ytitle="MSL Velocity (m/s)")
mslVel = gcurve(gdisplay=graphVel, color=color.orange)

#Acceleration
graphAcc = gdisplay(x=600, y=380, title="MSL Acceleration vs Time Graph", width=600, height=380, xtitle="Time (s)", ytitle="MSL Acceleration (m/s^2)")
mslAcc = gcurve(gdisplay=graphAcc, color=color.yellow)

#Force Air Drag
graphFa = gdisplay(x=0, y=0, title="Force of Air Drag vs Time Graph", width=600, height=380, xtitle="Time (s)", ytitle="Force of Air Drag (N)")
mslFa = gcurve(gdisplay=graphFa, color=color.white)

#Kinetic Energy
graphEk = gdisplay(x=600, y=0, title="Kinetic Energy vs Time Graph", width=600, height=380, xtitle="Time (s)", ytitle="Kinetic Energy (J)")
mslEk = gcurve(gdisplay=graphEk, color=color.green)

#Gravitational Potential Energy (Earth)
graphEp1 = gdisplay(x=0, y=380, title="Gravitational Potential Energy (Earth) vs Time Graph", width=600, height=380, xtitle="Time (s)", ytitle="Gravitational Potential Energy (J)")
mslEp1 = gcurve(gdisplay=graphEp1, color=color.green)

#Gravitational Potential Energy (Mars)
graphEp2 = gdisplay(x=600, y=380, title="Gravitational Potential Energy (Mars) vs Time Graph", width=600, height=380, xtitle="Time (s)", ytitle="Gravitational Potential Energy (J)")
mslEp2 = gcurve(gdisplay=graphEp2, color=color.green)

#Fuel Consumption
graphFuel = gdisplay(x=300, y=190, title="Fuel Consumption vs Time Graph", width=600, height=380, xtitle="Time (s)", ytitle="Fuel Consumption (kg)")
mslFuel = gcurve(gdisplay=graphFuel, color=color.green)

######################
# Defining Functions #
######################

#Defining a vector direction formula    
def direct(body1,body2):
    value = norm(body1.pos-body2.pos)
    return value

#Defining the radius formula
def dist(body1,body2):
    value = mag(body1.pos-body2.pos)
    return value

#Converting an x,y coordinate to radian angle using arctan
def xytotheta(x,y):
    if(x<0):     #In quadrant II or III
        value = pi+atan(y/x)
    elif(x>0 and y<0): #In quadrant IV
        value = 2*pi+atan(y/x)
    else:
        value = atan(y/x)
    return value

#Setting/Resetting planet positions & relative velocity vectors
def setplanets():
    for i in[0, 3, 4, 7]:
        bodies[i].pos = (bodies[i].orbit*cos(bodies[i].angle), bodies[i].orbit*sin(bodies[i].angle),0)
        bodies[i].velocity = vector(-(bodies[i].speed*sin(bodies[i].angle)), bodies[i].speed*cos(bodies[i].angle),0)
    msl.pos =       (earth.pos.x+earth.radius,earth.pos.y,0)
    msl.velocity =      vector(-(earth.speed*sin(earth.angle)),(earth.speed*cos(earth.angle))+msl.speed,0)
    moon.pos =      (moon.orbit*cos(moon.angle)+earth.pos.x, moon.orbit*sin(moon.angle)+earth.pos.y,0)
    moon.velocity =     vector((earth.velocity.x-(moon.speed*sin(moon.angle))),(earth.velocity.y+(moon.speed*cos(moon.angle))),0)
    deimos.pos =    (deimos.orbit*cos(deimos.angle)+mars.pos.x, deimos.orbit*sin(deimos.angle)+mars.pos.y,0)
    deimos.velocity =   vector((mars.velocity.x-(deimos.speed*sin(deimos.angle))),(mars.velocity.y+(deimos.speed*cos(deimos.angle))),0)
    phobos.pos =    (phobos.orbit*cos(phobos.angle)+mars.pos.x, phobos.orbit*sin(phobos.angle)+mars.pos.y,0)
    phobos.velocity =   vector((mars.velocity.x-(phobos.speed*sin(phobos.angle))),(mars.velocity.y+(phobos.speed*cos(phobos.angle))),0)

#Window control
c = controls(x=95, y=20, width=150, height=300, range=60)
readouts = display(title='Info', width=300, height=280, x=20, y=340)
scene = display(title='Main Window', width=800,height=600, x=340, y=20, background=(0,0,0))

############################
# Decleration of Variables #
############################

#Sun Constants [4]
sun1= local_light(pos=(0,0,0), color=color.yellow)
sun=sphere(pos=sun1.pos, color=sun1.color, material=materials.emissive)
sun.velocity=vector(0,0,0)
sun.mass=1.98892e30
sun.radius=6955e6

#Earth Constants [2]
earth=sphere(pos=(1*au,0,0), axis=(0,0,1), material=materials.earth)
earth.rotate(angle=pi/2, axis=(1,0,0), origin=earth.pos)
earth.speed = 29.79e3
earth.orbit=1*au
earth.mass=5.97e24
earth.radius=6378.5e3
pressure_initial=101325
temp_initial=288.15
L=0.0065
molar_mass=0.0289644
g=9.8
R=8.31447

#Moon Constants [3]
moon=sphere(pos=(1*au+405.7e6,0,0), color=color.white, material=materials.marble)
moon.speed = 1.018e3
moon.orbit = 384e6
moon.mass=7.3480e22
moon.radius=1.7375e6

#Mars Constants [5]
mars=sphere(pos=(1.53030994*au,0,0), color=(1,0.6,0), material=materials.marble)
mars.speed = 24.1e3
mars.orbit = 2.279e11
mars.mass=6.4191e23
mars.radius=3396.2e3

#Phobos Constants [8]
phobos=sphere(pos=(1.53030994*au+9520e3,0,0), color=color.blue, material=materials.rough)
phobos.speed = 2.138e3
phobos.orbit = 9379e3
phobos.mass=1.072e16
phobos.radius=11.1e5

#Deimos Constants [9]
deimos=sphere(pos=(1.53030994*au+23465e3,0,0), color=color.cyan, material=materials.rough)
deimos.speed = 1.351e3
deimos.orbit = 2.346e7
deimos.mass=1.48e15
deimos.radius=6.2e5

#Jupiter Constants [7]
jupiter=sphere(pos=(4.95155843*au,0,0),color=(1,0.6,0), material=materials.rough)
jupiter.speed = 13050
jupiter.orbit = 5.20336301*au
jupiter.mass=1.8986e27
jupiter.radius=71492e3

#Venus Constants [6]
venus=sphere(pos=(0,1.0821e11,0), color=color.blue, material=materials.marble)
venus.speed = 35.02e3
venus.orbit=1.0821e11
venus.mass = 4.8685e24
venus.radius=6052e3 

#Rockets & Thrusters
srb=sphere() #Aerojets
srb.num = 4
srb.mass = 40820
srb.dmdt = 528.95
srb.thrust = 1270e3 #N
srboost=True

ccb=sphere() #Common Core Booster
ccb.mass = 306914 #Kg
ccb.dmdt = 1360
ccb.thrust = 4152e3 #N
ccboost=True

cent=sphere() #Centaur
cent.mass = 18710
cent.dmdt = 22.42
cent.thrust = 99200
centboost = False

nk43=sphere()
nk43.mass = 1235 + 13000
nk43.thrust = 1753.8e3
nk43.dmdt = 540
nkburn = False
trburn = False
nkburn2=False


#MSL Variables [1]
msl=cylinder(pos=(earth.pos.x+6551e3,earth.pos.y,0),color=color.yellow)
msl.speed=463.8576
msl.radius=50
msl.axis = 400*direct(earth,msl)
msl.mass = 3000 + ccb.mass + 4*srb.mass + cent.mass + nk43.mass
C_d=0.4
A=11.9695

###########################################
# Calculating the angles for start points #
###########################################
mars.angle = xytotheta(-1.433935166076733e8,  1.994373783952959e8)  
moon.angle = xytotheta(2.105038832399641e5, 3.418251526757990e5)    
earth.angle = xytotheta(3.470214891786226e7, 1.432067773090643e8)
jupiter.angle = xytotheta(5.788498190240492e8,  4.661451550913818e8)    
deimos.angle = xytotheta(1.946315087104524e4,  9.814006413521352e3)
phobos.angle = xytotheta(-1.844194617710594e3, -9.186398125370371e3)
venus.angle = xytotheta(9.040560727457863e7, -6.043516111307473e7)

#Creates a list of the planets; useful for iterative loops
bodies = array([earth,msl,moon,mars,jupiter,phobos,deimos,venus,sun])

##Camera view changing controls
def camerapos(number):
    cm.body = number
cm = menu(pos=(0,45), height=10, width=40, text='Camera Pos')
cm.body = int()
cameras = [earth.pos, moon.pos, msl.pos, mars.pos, jupiter.pos, venus.pos, sun.pos]
cm.items=(('Earth',lambda:camerapos(0)),('Moon',lambda:camerapos(1)),('MSL',lambda:camerapos(2)),('Mars',lambda:camerapos(3)),('Jupiter',lambda:camerapos(4)),('Venus',lambda:camerapos(5)),('Sun',lambda:camerapos(6)))
t1 = toggle(pos=(0,-35), width=5, length=20, text0='Stop', text1='Run')
s1 = slider(pos=(15,-45), width=5, length=70, axis=(0,1,0), min=1, max=10000) #rate changer
messagebox=label(display=readouts)

#Placing the trail & planet start points
setplanets()
    
#Planet Labels
sunlabel=label(pos=sun.pos, text='Sun', yoffset=20)
earthlabel=label(pos=earth.pos, text='Earth', yoffset=20)
marslabel=label(pos=mars.pos, text='Mars', yoffset=20)
jupiterlabel=label(pos=jupiter.pos, text='Jupiter', yoffset=20)
venuslabel=label(pos=venus.pos, text='Venus', yoffset=20)

#############
# Idle Loop #
#############
while(1==1):
    rate(50)
    c.interact()
    scene.center=cameras[cm.body]
    #Placing the trail & planet start points
    setplanets()
    for i in range(0,9):
        bodies[i].trail = curve(pos=(bodies[i].pos), color=(bodies[i].color))
    #Values to be reset with toggle reset
    t=0
    d=0
    TMI=2
    #######################################
    # Loop for Launching into mars' orbit #
    #######################################
    while(t1.value==1):
        c.interact()
        scene.center=cameras[cm.body] #Drop down menu camera change
        earth.rotate(angle=(2*pi/(86400))*dt, axis=(0,0,1), origin=earth.pos)
        ##----Air Drag-----############
        h=mag(earth.pos-msl.pos)-earth.radius
        vel_fluid=mag(earth.velocity-msl.velocity)
        temp=temp_initial-L*h
        if h <= 44300:
            pressure=pressure_initial*(1-(L*h)/temp_initial)**(g*molar_mass/(R*L))
        #If it gets higher than 44km, pressure is negligible
        else:
            pressure=0
        density=pressure*molar_mass/(R*temp)
        drag_force=0.5*density*(vel_fluid**2)*C_d*A
        ##-----------------############
        t=t+dt
        d=d+dt
        rate(s1.value) ##Controllable Rate
    ####----Launch statements-----####
        #mslangle = -xytotheta((msl.pos.x-earth.pos.x),(msl.pos.y-earth.pos.y))
        #perptoearth = vector(-sin(mslangle),cos(mslangle),0)
        if(TMI==2):
            #if it hasn't used up all it's fuel
            if srb.mass>(4100) and srboost==True:
                srb.mass -= srb.dmdt*dt
                msl.mass -= srb.dmdt*srb.num*dt
            #if it has, dump the booster
            elif srb.mass<(4100) and srboost==True:
                msl.mass -= srb.mass*srb.num
                srb.mass = 0
                srb.thrust = 0
                msl.rotate(angle=(pi/4-.2), axis=(0,0,1),origin=msl.pos)
                print 'h: ' + str(h) + ' m'
                srboost = False
            if ccb.mass>23000 and ccboost==True:
                ccb.mass -= ccb.dmdt*dt
                msl.mass -= ccb.dmdt*dt
                msl.rotate(angle=2e-4, axis=(0,0,1))
            elif ccb.mass<23000 and ccboost==True:
                msl.mass -= ccb.mass
                ccb.mass = 0
                ccb.thrust = 0
                print 'h: ' + str(h) + ' m'
                ccboost = False
                centboost=True
            if centboost==True and cent.mass>=2000 and dist(earth,msl)<7570000:
                cent.mass -= cent.dmdt*dt
                msl.mass -= cent.dmdt*dt
                msl.rotate(angle=1.1e-4, axis=(0,0,1))
            elif centboost==True and dist(earth,msl)>7570000:
                msl.mass -= cent.mass
                centboost=False
                print 'Centaur Mass: ' + str(cent.mass) + ' kg'
                cent.mass = 0
                cent.thrust = 0
                print(mag(earth.velocity-msl.velocity))
                dt=1
                ##--Launch or not--##
                TMI=1
                ##-----------------##
                d=0
                print '\nTo Mars!'
                
    ####-------------------####
                #2pi ~ 5500
                #pi/2 ~ 7000s
        mslangle = xytotheta((mars.pos.x-msl.pos.x),(mars.pos.y-msl.pos.y))
        perptomars = vector(-sin(mslangle),cos(mslangle),0)
        marsh=(dist(mars,msl)-mars.radius)
        if(TMI<=1):
            msl.axis=400*norm(msl.velocity)
            if 23.3e6>d>=8700:
                dt=.1
            if((d>=8743) and (TMI==1)):
                msl.axis=400*norm(msl.velocity-earth.velocity)
                #if it hasn't reached neccesary velocity
                if((mag(earth.velocity-msl.velocity))<vescape):
                    dt=0.5
                    nkburn = True
                elif((mag(earth.velocity-msl.velocity))>=vescape and TMI==1):
                    TMI=0
                    print 'NK43 mass: ' + str(nk43.mass) + ' kg'
                    #msl.mass -= cent.mass
                    nkburn = False
                    cent.mass = 0
                    dt=1
            if(mag(msl.pos-earth.pos)>1.5e7 and dist(mars,msl)>23000000): #we don't have all day
                dt=500
            #dist(mars,msl)~3,600,000. orb vel~3450
            #When the craft gets to mars' orbit radius, boost to orbital velocity
            if((dist(mars,msl))<22000000 and (deltav>=1)):
                trburn=True
                msl.axis=400*perptomars
                dt=1
                deltav=2
                if(mag(mars.velocity-msl.velocity)<sqrt(G*mars.mass/dist(msl,mars))):
                    print 'Distance from Mars: ' + str(dist(msl,mars)) + ' m'
            if(mars.velocity.y-msl.velocity.y<-1210 and deltav==2):
                trburn=False
                dt = 1
                #print msl.velocity.mag
                deltav=0
            if (marsh/1000)<800 and mag(mars.velocity-msl.velocity)>4000:# and mag(mars.velocity-msl.velocity)
                nkburn2=True
                msl.axis=norm(msl.velocity)
            else:
                nkburn2=False
                
        #Calculating accelerations
        a12 = (G*earth.mass/dist(earth,msl)**2)*direct(earth,msl) 
        a14 = (G*sun.mass/dist(sun,msl)**2)*direct(sun,msl)
        a13 = (G*moon.mass/dist(moon,msl)**2)*direct(moon,msl)
        a15 = (G*mars.mass/dist(mars,msl)**2)*direct(mars,msl)
        a16 = (G*venus.mass/dist(venus,msl)**2)*direct(venus,msl)
        a18 = (G*phobos.mass/dist(phobos,msl)**2)*direct(phobos,msl)
        a19 = (G*deimos.mass/dist(deimos,msl)**2)*direct(deimos,msl)
        a17 = (G*jupiter.mass/dist(jupiter,msl)**2)*direct(jupiter,msl)
        a24 = (G*(sun.mass)/dist(sun,earth)**2)*direct(sun,earth)
        a32 = (G*(earth.mass)/dist(moon,earth)**2)*direct(earth,moon)
        a34 = (G*(sun.mass)/dist(sun,moon)**2)*direct(sun,moon)
        a54 = (G*sun.mass/dist(sun,mars)**2)*direct(sun,mars)
        a64 = (G*sun.mass/dist(sun,venus)**2)*direct(sun,venus)
        a74 = (G*sun.mass/dist(sun,jupiter)**2)*direct(sun,jupiter)
        a85 = (G*mars.mass/dist(mars,phobos)**2)*direct(mars,phobos)
        a84 = (G*sun.mass/dist(sun,phobos)**2)*direct(sun,phobos)
        a95 = (G*mars.mass/dist(mars,deimos)**2)*direct(mars,deimos)
        a94 = (G*sun.mass/dist(sun,deimos)**2)*direct(sun,deimos)
        alaunch = -((srb.thrust*srb.num + ccb.thrust)/msl.mass)*norm(msl.axis)
        leorbit = -((cent.thrust/msl.mass)*norm(msl.axis))
        trforce = (nk43.thrust/msl.mass)*norm(vector(0, 1, 0))
        nk43force = (nk43.thrust/msl.mass)*norm(msl.axis)
        dragforce = ((drag_force/msl.mass)*norm(earth.velocity-msl.velocity))

        kineticenergy = 0.5*msl.mass*(mag(msl.velocity)**2)
        gravenergy1 = -(G*earth.mass*msl.mass/dist(earth,msl))
        gravenergy2 = -(G*mars.mass*msl.mass/dist(mars,msl))
        
        msl.accel = a12+a13+a14+a15+a16+a19+a18+a17+alaunch+dragforce
        if centboost == True:
            msl.accel = a12+a13+a14+a15+a19+a18+a17+leorbit+dragforce
        if nkburn==True and nk43.mass>1300:
            msl.accel = a12+a13+a14+a15+a19+a18+a17+a16+nk43force
            nk43.mass -= nk43.dmdt*dt
            msl.mass -= nk43.dmdt*dt
        if trburn==True and nk43.mass>1300:
            msl.accel = a12+a13+a14+a15+a19+a18+a17+a16+trforce
            nk43.mass -= nk43.dmdt*dt
            msl.mass -= nk43.dmdt*dt
        if nkburn2==True:# and nk43.mass>1200:
            msl.accel = a12+a13+a14+a15+a19+a18+a17+a16+nk43force
        earth.accel = a24
        moon.accel = a32+a34
        mars.accel = a54
        phobos.accel =  a85+a84
        deimos.accel = a95+a94
        jupiter.accel = a74
        venus.accel = a64

        #Updating the planetary positions
        for i in range(0,8):
            bodies[i].velocity = bodies[i].velocity + bodies[i].accel*dt
            bodies[i].pos = bodies[i].pos + bodies[i].velocity*dt

        #Plotting the graphs
        #stage1: if t<208.8:
        #stage2: if centboost==True:
        #stage3: if nkburn==True:
        mslPos1.plot(pos=(t,dist(earth,msl)))
        mslPos2.plot(pos=(t,dist(mars,msl)))
        mslVel.plot(pos=(t,mag(msl.velocity)))
        mslAcc.plot(pos=(t,mag(msl.accel)))
        mslFuel.plot(pos=(t,(506139-msl.mass)))
        mslEk.plot(pos=(t,kineticenergy))
        if t<100:
            mslFa.plot(pos=(t,drag_force))
        if t<1500:
            mslEp1.plot(pos=(t,gravenergy1))
        if t>4e6:
            mslEp2.plot(pos=(t,gravenergy2))

        #Planetary trails
        for i in range(0,8):
            bodies[i].trail.append(pos=bodies[i].pos)
        messagebox.text = 'Everything you need to know:'
        messagebox.text +=  '\nMSL Mass: ' + str(msl.mass) + ' kg'
        messagebox.text += '\nSRB Mass: ' + str(srb.mass) + ' kg'
        messagebox.text += '\nCCB Mass: ' + str(ccb.mass) + ' kg'
        messagebox.text += '\nCentaur Mass: ' + str(cent.mass) + ' kg'
        messagebox.text += '\nNK43 Mass: ' + str(nk43.mass) + ' kg'
        messagebox.text += '\nMSL Acceleration: ' + str(mag(msl.accel)) + ' m/s^2'
        messagebox.text += '\nMSL Velocity: ' + str(mag(earth.velocity-msl.velocity)) + ' m/s'
        messagebox.text += '\nTime: ' + str(t) + ' sec'
        messagebox.text += '\nDays: ' + str(t/86400)
        messagebox.text += '\nHeight from Earth: ' + str((dist(earth,msl)-earth.radius)/1000) + ' km'
        messagebox.text += '\nHeight from Mars:' + str(marsh/1000) + ' km'
