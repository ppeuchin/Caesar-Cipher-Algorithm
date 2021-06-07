from colorama import init, Fore, Back, Style

init()

def print_with_color(text, color=Fore.WHITE, brightness=Style.NORMAL):
    print(f'{brightness}{color}{text}{Style.RESET_ALL}')