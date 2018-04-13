import sys, _header

# Import Leap
try:
    import Leap

    from models.GestureListener import GestureListener
    from models.PositionListener import PositionListener
except:
    print "Error: Leap Importation"
    sys.exit()

def main():
    # Create a listener and controller
    #listener = GestureListener()
    listener = PositionListener()
    controller = Leap.Controller()

    # Refer the Listener to the Controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()