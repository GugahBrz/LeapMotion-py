import sys, _header

# Import Libraries
try:
    import Leap
except:
    print "Error: Leap Importation"
    sys.exit()

class GameListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"
        self.frame = None

    def on_frame(self, controller):
        self.frame = controller.frame()
        if len(self.frame.hands) != 0: 
            self.gesture_listener()
            
    def gesture_listener(self):

        fingers = self.frame.hands[0].pointables
        thumb = fingers[0]
        index = fingers[1]
        middle = fingers[2]
        ring = fingers[3]
        pinky = fingers[4]

        if( not middle.is_extended 
            and not index.is_extended 
            and not thumb.is_extended 
            and not ring.is_extended 
            and not pinky.is_extended ):
            print "Rock"
        
        if( middle.is_extended 
            and index.is_extended
            and thumb.is_extended 
            and ring.is_extended 
            and pinky.is_extended ):
            print "Paper"

        if( (middle.is_extended and index.is_extended) 
            and (not thumb.is_extended 
            and not ring.is_extended 
            and not pinky.is_extended) ):
            print "Scissor"

def main():

    # Create a listener and controller
    listener = GameListener()
    controller = Leap.Controller()

    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

# Call the main function
if __name__ == "__main__":
    main()