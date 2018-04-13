import sys, _header, requests

# Important links
# https://forum.poppy-project.org/t/utiliser-rest-apis/2255
# https://forum.poppy-project.org/t/poppy-rest-web-services-and-clients/825

def leds() :
    # Leds
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m6:led:red")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m5:led:green")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m4:led:yellow")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m3:led:blue")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m2:led:pink")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m1:led:cyan")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m6:led:white")

def reset_leds() :
    # Leds
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m6:led:off")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m5:led:off")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m4:led:off")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m3:led:off")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m2:led:off")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m1:led:off")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m6:led:off")

def motors() :
    # Motors: Goal_Position
    # m1
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m1:goal_position:50")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m1:goal_position:0")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m1:goal_position:-50")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m1:goal_position:0")

    # m2
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m2:goal_position:-30")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m2:goal_position:0")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m2:goal_position:30")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m2:goal_position:0")

def reset_motors() :
    # All to 0
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m6:goal_position:0")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m5:goal_position:0")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m4:goal_position:0")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m3:goal_position:0")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m2:goal_position:0")
    reponse = requests.get("http://poppy.local:6969/motors/set/registers/m1:goal_position:0")

def main() :
    leds()
    reset_motors()
    motors()

    ## http://<nom_du_robot>:6969/ik/<chain>/goto/<x-left-right>/<y-front-back>/<z-top-down>/<duree>
    # reponse = requests.get("http://poppy.local:6969/ik/chain/goto/0/0/0/1")

if __name__ == "__main__" :
    main()