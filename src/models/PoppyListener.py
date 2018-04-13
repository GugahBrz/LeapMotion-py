import sys, _header, requests

# Import Libraries
try:
    import Leap
except:
    print "Error: Leap Importation"
    sys.exit()

class PoppyListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"
        self.frame = None

    def on_frame(self, controller):
        self.frame = controller.frame()
        number_of_hands = len(self.frame.hands)
        if number_of_hands != 0:
            self.gesture_listener()
            
    def gesture_listener(self):

        for hand in self.frame.hands:
            xaxis = (hand.palm_position[0]/100)
            yaxis = (hand.palm_position[1]/100)
            zaxis = (hand.palm_position[2]/100)

        reponse = requests.get("http://poppy.local:6969/ik/chain/goto/"+str(xaxis)+"/"+str(yaxis)+"/"+str(zaxis)+"/1")