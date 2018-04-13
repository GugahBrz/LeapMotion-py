# -*- coding: utf-8 -*-
import sys
import math

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ''' Error: PyOpenGL not installed properly !!'''
  sys.exit(  )

class Camera( object ):
    def __init__(self, stereo="PARALLEL",fovy=60.0) :
        self.width=800.0
        self.height=800.0
        self.fovy=fovy*math.pi/180.0
        self.ratio=1.0 # self.width/self.height
        self.zDist=50.0 # Distance in the scene from the camera to the display plane.
        self.dip=0.5  # Camera inter-axial separation (eye separation).
        self.near=0.1 # Distance in the scene from the camera to the near plane.
        self.far = 500.0 # Distance in the scene from the camera to the far plane.
        self.convergence=self.far
        self.update_right()
        self.update_left()

    def update_left(self, stereo= "PARALLEL") :
        self.lookAtLeft = (-self.dip/2, 0, self.zDist, -self.dip/2, 0, 0,  0, 1, 0 )
        ratio=self.width/self.height
        top =   self.near*math.tan(self.fovy/2.0)
        bottom = -top
        a=ratio*math.tan(self.fovy/2.0)*self.convergence
        b=a-(self.dip/2.0)
        c=a+(self.dip/2.0)
        if self.convergence != 0.0 :
            left =  -b*(self.near/self.convergence)
            right =  c*(self.near/self.convergence)
        else :
            left =  -b*(self.near/0.1)
            right =  c*(self.near/0.1)
        self.frustumLeft = (left, right, bottom, top, self.near, self.far  )
        

    def update_right(self, stereo= "PARALLEL") :
        self.lookAtRight = (self.dip/2, 0, self.zDist, self.dip/2, 0, 0,  0, 1, 0 )
        ratio=self.width/self.height
        top =   self.near*math.tan(self.fovy/2.0)
        bottom = -top
        a=ratio*math.tan(self.fovy/2.0)*self.convergence
        b=a-(self.dip/2.0)
        c=a+(self.dip/2.0)
        if self.convergence != 0.0 :
            left  = -c*(self.near/self.convergence)
            right =  b*(self.near/self.convergence)
        else :
            left  =  -c*(self.near/0.1)
            right =  b*(self.near/0.1)
        self.frustumRight = (left, right, bottom, top, self.near, self.far  )

    def get_dip(self) :
        return self.dip

    def set_dip(self, dip) :
        self.dip=dip

    def get_distance(self) :
       return self.zDist

    def set_distance(self, z) :
        self.zDist=z

if __name__ == '__main__' :
	camera = Camera()
