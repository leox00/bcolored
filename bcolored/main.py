class TextColor:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

current_color = TextColor.RESET

def change_color(color):
    global current_color
    if color == "red":
        current_color = TextColor.RED
    elif color == "green":
        current_color = TextColor.GREEN
    elif color == "yellow":
        current_color = TextColor.YELLOW
    elif color == "blue":
        current_color = TextColor.BLUE
    elif color == "purple":
        current_color = TextColor.PURPLE
    elif color == "cyan":
        current_color = TextColor.CYAN
    elif color == "white":
        current_color = TextColor.WHITE
    else:
        print("Invalid color!")

def print_colored(text):
    print(current_color + text + TextColor.RESET)

def input_colored(text):
    return input(current_color + text + TextColor.RESET)