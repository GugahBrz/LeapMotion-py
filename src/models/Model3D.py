# -*- coding: utf-8 -*-
from sys import argv, exit
from time import sleep
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
  import math
except:
  print ''' Error: PyOpenGL not installed properly !!'''
  sys.exit()

class Model3D( object ) :
    def __init__(self) :
        self.create_model()

    def create_base(self, size) :		
         glutSolidCube(size)

    def draw_cube(self,length,pos):
      glPushMatrix()
      OpenGL.GL.glTranslate(0.1*pos.x,0.1*pos.y,0.1*pos.z)
      glutSolidCube(length)
      glPopMatrix()

    def create_disk(self, size) :
        slices=20;
        stacks=30;
        params = gluNewQuadric();
        gluQuadricDrawStyle(params,GLU_FILL);
        gluQuadricTexture(params,GL_TRUE);
        gluDisk(params, 0, size, slices, stacks)
        gluDeleteQuadric(params);

    def create_sphere(self, radius, longitude,latitude) :
        params = gluNewQuadric()
        gluQuadricDrawStyle(params,GLU_FILL)
        gluQuadricTexture(params,GL_TRUE)
        gluQuadricNormals(params, GLU_SMOOTH); 
        gluQuadricOrientation(params,GLU_OUTSIDE);
        gluSphere(params,radius, longitude,latitude)
        gluDeleteQuadric(params)

    def draw_sphere(self,radius,pos):
        glPushMatrix()
        OpenGL.GL.glTranslate(0.1*pos.x,0.1*pos.y,0.1*pos.z)
        glutSolidSphere(radius,20,30)
        glPopMatrix()

    def create_cylinder(self,base,top,height) :
        slices=20;
        stacks=30;
        params = gluNewQuadric();
        gluQuadricDrawStyle(params,GLU_FILL);
        gluQuadricTexture(params,GL_TRUE);
        gluCylinder(params,base,top,height,slices,stacks);
        gluDeleteQuadric(params);

    def draw_line(self,radius,pos):
        glPushMatrix()
        OpenGL.GL.glTranslate(0.1*pos.x,0.1*pos.y,0.1*pos.z)
        glutSolidSphere(radius,20,30)
        glPopMatrix()

    def create_joint(self, radius) :
        latitude=10;
        longitude=20;
        self.create_sphere(radius,longitude,latitude);

    def create_link(self, size) :
        base=0.1*size
        top=0.1*size
        self.create_cylinder(base,top,size)
        self.create_disk(size)
    def create_model(self, size=1) :
         self.create_sphere(size,10,20)
 
    def create_axe(self, size=1) :
         self.create_cylinder(0.08*size,0.08*size,size)
         glPushMatrix()
         glTranslatef(0, 0, size);
         self.create_cylinder(0.1*size,0,0.25*size)
         glPopMatrix()

    def world_coordinate_system(self,size) :
        glColor3ub(255,0,0) #face rouge (Oz)
        self.create_axe(size)
        glPushMatrix()
        glRotatef(-90.0, 1, 0, 0);
        glColor3ub(0,0,255) #face bleue (Oy)
        self.create_axe(size)
        glPopMatrix()
        glPushMatrix()
        glRotatef(90.0, 0, 1, 0);
        glColor3ub(0,255,0) #face vert (Ox)
        self.create_axe(size)
        glPopMatrix()