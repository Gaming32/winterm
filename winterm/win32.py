import ctypes
kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32


class COORD(ctypes.Structure):
    _fields_ = [
        ('X', ctypes.c_short),
        ('Y', ctypes.c_short),
    ]

class SMALL_RECT(ctypes.Structure):
    _fields_ = [
        ('Left',   ctypes.c_short),
        ('Top',    ctypes.c_short),
        ('Right',  ctypes.c_short),
        ('Bottom', ctypes.c_short),
    ]

class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [
        ('dwSize',              COORD),
        ('dwCursorPosition',    COORD),
        ('wAttributes',         ctypes.c_ushort),
        ('srWindow',            SMALL_RECT),
        ('dwMaximumWindowSize', COORD),
    ]


def GetConsoleCursorPosition(hConsoleOutput):
    cbsi = CONSOLE_SCREEN_BUFFER_INFO()
    success = GetConsoleScreenBufferInfo(hConsoleOutput, cbsi)
    if success:
        return cbsi.dwCursorPosition
    return success


GetStdHandle = kernel32.GetStdHandle
SetConsoleCursorPosition = kernel32.SetConsoleCursorPosition
GetConsoleScreenBufferInfo = kernel32.GetConsoleScreenBufferInfo