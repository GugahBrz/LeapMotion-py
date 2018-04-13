import sys, _header

# Import Libraries
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *

    from models.Hand import Hand
except:
    print "Error: Importation"
    sys.exit()

# The main function
def main():

    # Initialize OpenGL
    glutInit(sys.argv)
    # Set display mode
    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
    # Set size and position of window size
    glutInitWindowSize(1200, 1000)
    glutInitWindowPosition(100, 100)

    # Create window with given title
    title = "Leap OpenGl Integration"
    glutCreateWindow(title)

    # Render the hand   
    myHand = Hand()

    # The callback for display function
    glutDisplayFunc(myHand.display)
    # The callback for reshape function
    glutReshapeFunc(myHand.reshape)
    # The callback that animate the hand
    glutIdleFunc(myHand.animate)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()    

# Call the main function
if __name__ == "__main__":
    main()