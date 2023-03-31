"""
    All tools needed for this project;
"""


from os import name
from os import system


OS_NAME = name


def clear():
    """
        :ARGS:
            none;

        :RETURNS:
            return None;

        :INFO:
            wipe the terminal screen;
    """

    if OS_NAME == "posix":
        # for *nix machines;
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for any system in this world;
        # system("your-clear-command-here")
        pass

    return None
