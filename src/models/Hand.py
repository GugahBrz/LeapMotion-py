import sys, _header

# Import Libraries
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *

    import Leap

    from Model3D import Model3D
    from Camera import Camera
    from Light import Light
except:
    print "Error: Importation"
    sys.exit()

class Hand :
    
    def __init__(self) :

        # Create a controller for leap
        self.controller = Leap.Controller()

        # From classes
        self.model = Model3D()
        self.camera = Camera()
        self.light = Light()

        # Common variables
        self.rotate = 0.0

    def display(self) :
        glClearColor(0.0,0.0,0.0,0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        # Render and Draw entities
        self.render()
        self.draw_hands()

        glutSwapBuffers()
       
    def reshape(self, w, h) :
        glutPostRedisplay()

    def render(self) :
        glViewport(0,0, glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60,1,0.1,100)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0,0,100,0,0,0,0,1,0)

    def draw_hands(self) :
        # Rotate Camera to 
        glRotate(30.0,1.0,0.0,0.0)
        glPushMatrix()
        glRotate(self.rotate,0.0,1.0,0.0)
        
        # Create X,Y,Z visual cordinates
        self.model.world_coordinate_system(5)
        glPopMatrix()
        
        # Get hands from Leap
        frame =  self.controller.frame()
        hands = frame.hands

        for hand in hands:
            # Look at hand
            center = hand.sphere_center
            glPushMatrix()
            glTranslate(0.1*center.x, 0.1*center.y, 0.1*center.z)
            glPopMatrix()

            # Draw Fingers
            for finger in hand.fingers:
                for b in range(0,4):
                    pos = finger.bone(b).center
                    self.model.draw_sphere(1,pos)

    def animate(self) :
        glutPostRedisplay()