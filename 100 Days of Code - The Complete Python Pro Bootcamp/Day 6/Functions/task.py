while at_goal() is False:
    if front_is_clear():
        move()
        turn_left()
    elif wall_in_front():
        turn_right()
    elif wall_on_right() and wall_in_front():
        turn_around()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
