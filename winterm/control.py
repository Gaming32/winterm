import sys
from .constants import get_handle_constant
from .win32 import COORD, GetStdHandle, SetConsoleCursorPosition


def move_cursor(x, y, stream=sys.stdout):
    handleid = get_handle_constant(stream)
    handle = GetStdHandle(handleid)
    position = COORD(x, y)
    return SetConsoleCursorPosition(handle, position)


def get_cursor_position(stream=sys.stdout):
    pass