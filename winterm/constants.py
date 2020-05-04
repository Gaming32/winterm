import sys


STD_INPUT_HANDLE  = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE  = -12


def get_handle_constant(stream):
    if stream is sys.__stdout__:
        return STD_OUTPUT_HANDLE
    elif stream is sys.__stdin__:
        return STD_INPUT_HANDLE
    elif stream is sys.__stderr__:
        return STD_ERROR_HANDLE
    else:
        return None