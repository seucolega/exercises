"""
Ghost Gobble Arcade Game on Exercism's Python Track
"""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Define if Pac-Man eats a ghost

    :param power_pellet_active: bool - does the player have an active power
     pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Define if Pac-Man scores

    :param touching_power_pellet: bool - does the player have an active power
    pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Define if Pac-Man loses

    :param power_pellet_active: bool - does the player have an active power
     pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    return touching_ghost and not power_pellet_active


def win(
        has_eaten_all_dots: bool, power_pellet_active: bool,
        touching_ghost: bool
) -> bool:
    """Define if Pac-Man wins

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power
    pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    return has_eaten_all_dots and (power_pellet_active or not touching_ghost)
