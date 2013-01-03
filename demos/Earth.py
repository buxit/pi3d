# Earth and example shapes using pi3d module
# ==========================================
# Copyright (c) 2012 - Tim Skillman
# Version 0.03 - 20Jul12
#
# This example does not reflect the finished pi3d module in any way whatsoever!
# It merely aims to demonstrate a working concept in simplfying 3D programming on the Pi
#
# PLEASE INSTALL PIL imaging with:
#
#      $ sudo apt-get install python-imaging
#
# before running this example
#
from math import sin, cos

from pi3d import Display
from pi3d.Keyboard import Keyboard
from pi3d.Texture import Texture

from pi3d.context.Light import Light
from pi3d.Camera import Camera
from pi3d.Shader import Shader

from pi3d.shape.Sphere import Sphere
from pi3d.shape.Plane import Plane

from pi3d.util import Draw
from pi3d.util.Screenshot import screenshot

# Setup display and initialise pi3d
DISPLAY = Display.create(x=50, y=50)
DISPLAY.set_background(0,0,0,1)    	# r,g,b,alpha

light = Light((10, 10, -20))
shader = Shader("shaders/uv_reflect")
flatsh = Shader("shaders/uv_flat")
#========================================

# Setting 2nd param to True renders 'True' Blending
# (this can be changed later to 'False' with 'cloudimg.blend = False')
cloudimg = Texture("textures/earth_clouds.png",True)
earthimg = Texture("textures/world_map.jpg")
moonimg = Texture("textures/moon.jpg")
starsimg = Texture("textures/stars2.jpg")
watimg = Texture("textures/water.jpg")

mysphere = Sphere(light=light, radius=2, slices=24, sides=24,
                  name="earth", z=5.8)
mysphere2 = Sphere(light=light, radius=2.05, slices=24, sides=24,
                   name="clouds", z=5.8)
mymoon = Sphere(light=light, radius=0.4, slices=16, sides=16, name="moon")
mymoon2 = Sphere(light=light, radius=0.1, slices=16, sides=16, name="moon2")
myplane = Plane(light=light, w=50, h=50, name="stars", z=10)

# Fetch key presses
mykeys = Keyboard()

rot=0.0
rot1=90.0
rot2=0.0
m1Rad = 4 # radius of moon orbit
m2Rad = 0.55 # radius moon's moon orbit


# Display scene
while DISPLAY.loop_running():
  myplane.draw(flatsh,[starsimg], 0.0, -1.0)
  myplane.rotateIncZ(0.01)

  mysphere.draw(shader, [earthimg])
  mysphere.rotateIncY(-0.1)
  mysphere2.draw(shader, [cloudimg])
  mysphere2.rotateIncY(-0.15)

  mymoon.draw(shader, [moonimg, moonimg, starsimg], 1.0, 0.0)
  mymoon.position(mysphere.unif[0] + m1Rad*sin(rot1), mysphere.unif[1] + 0, mysphere.unif[2] - m1Rad*cos(rot1))
  mymoon.rotateIncY(-0.2)

  mymoon2.draw(shader, [watimg, watimg, starsimg], 4.0, 0.8)
  mymoon2.position(mymoon.unif[0] - m2Rad*sin(rot2), mymoon.unif[1], mymoon.unif[2] + m2Rad*cos(rot2))
  mymoon2.rotateIncY(-5.0)

  rot1 += 0.005
  rot2 += 0.021

  k = mykeys.read()
  if k >-1:
    if k==112: screenshot("earthPic.jpg")
    elif k==27:
      mykeys.close()
      DISPLAY.stop()
      break
    else:
      print k

  Camera.instance().was_moved = False
