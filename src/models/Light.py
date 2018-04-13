from sys import argv, exit
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
  import math
except:
  print ''' Error: PyOpenGL not installed properly !!'''
  sys.exit()

class Light :
    def __init__(self) :
        glEnable( GL_LIGHTING )
        glEnable( GL_LIGHT0 )
        glLightModeli( GL_LIGHT_MODEL_TWO_SIDE, 0 )
        glLightfv( GL_LIGHT0, GL_POSITION, [4, 4, 4, 1] )
        lA = 0.8
        glLightfv( GL_LIGHT0, GL_AMBIENT, [lA, lA, lA, 1] )
        lD = 1
        glLightfv( GL_LIGHT0, GL_DIFFUSE, [lD, lD, lD, 1] )
        lS = 1
        glLightfv( GL_LIGHT0, GL_SPECULAR, [lS, lS, lS, 1] )
        glMaterialfv( GL_FRONT_AND_BACK, GL_AMBIENT, [0.2, 0.2, 0.2, 1] )
        glMaterialfv( GL_FRONT_AND_BACK, GL_DIFFUSE, [0.7, 0.7, 0.7, 1] )
        glMaterialfv( GL_FRONT_AND_BACK, GL_SPECULAR, [0.5, 0.5, 0.5, 1] )
        glMaterialf( GL_FRONT_AND_BACK, GL_SHININESS, 50 )

        self.lightColors = {
            "white":(1.0, 1.0, 1.0, 1.0),
            "red":(1.0, 0.0, 0.0, 1.0),
            "green":(0.0, 1.0, 0.0, 1.0),
            "blue":(0.0, 0.0, 1.0, 1.0),
            "cyan":(0.0, 0.5, 0.5, 1.0)
        }
        self.lightPosition = (5.0, 5.0, 20.0, 1.0)

    def setLightColor(self,color):
        """Set light color to 'white', 'red', 'green' or 'blue'."""
        if self.lightColors.has_key(color):
            color= self.lightColors[color]
            glLightfv( GL_LIGHT0, GL_AMBIENT, color)
            glLightfv( GL_LIGHT0, GL_DIFFUSE, color)
            glLightfv( GL_LIGHT0, GL_SPECULAR, color)


