import sys, _header

# Import Libraries
try:
    import Leap
    from Leap import CircleGesture, SwipeGesture, KeyTapGesture, ScreenTapGesture
except:
    print "Error: Importation"
    sys.exit()

class GestureListener(Leap.Listener):

    def on_connect(self, controller):
        print "Leap Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)

    def on_frame(self, controller):
        for gesture in controller.frame().gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                print "Gesture Recognized: Circle"
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                print "Gesture Recognized: Swipe"
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                print "Gesture Recognized: Key Tap"
            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                print "Gesture Recognized: Screen Tap"
        
