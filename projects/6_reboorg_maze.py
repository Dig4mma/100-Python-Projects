# Instruction of how to Escape maze in Reeborg's world!
# you can View the challenge on: "https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"
# you can use the code bewlow on that challenge and see how it works!

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    while wall_on_right():
        if front_is_clear() == True:
            move()
        elif wall_in_front():
            turn_left()
    while right_is_clear():
        turn_right()
        if not at_goal():
            move()
"""