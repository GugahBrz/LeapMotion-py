import sys, _header

# Import Libraries
try:
    import Leap
except:
    print "Error: Leap Importation"
    sys.exit()

class PositionListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"
        self.frame = None

    def on_frame(self, controller):
        self.frame = controller.frame()
        number_of_hands = len(self.frame.hands)
        if number_of_hands == 0: 
            print 'No Hands'
        else:
            self.gesture_listener()
            
    def gesture_listener(self):

        for hand in self.frame.hands:
            xaxis = hand.palm_position[0]
            yaxis = hand.palm_position[1]
            zaxis = hand.palm_position[2]

        if xaxis > 100:
            print 'Moving Right'
        elif xaxis < -100:
            print 'Moving Left'
        elif yaxis > 300:
            print 'Moving Up'
        elif yaxis < 200:
            print 'Moving Down'
        elif zaxis > 80:
            print 'Moving Back'
        elif zaxis < 0:
            print 'Moving Forward'
        else:
            print 'Stopped Moving'