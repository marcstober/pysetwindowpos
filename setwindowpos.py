from ctypes import *
from ctypes.wintypes import HWND, UINT

# TODO: publish on pypi?
# TODO: only export what I actually want to

def set_window_topmost(hwnd):
    HWND_TOPMOST = -1
    SWP_NOSIZE = 0x0001
    SWP_NOMOVE = 0x0002
    user32 = WinDLL("user32", use_last_error=True)
    SetWindowPos = user32.SetWindowPos
    SetWindowPos.argtypes = [HWND, HWND, c_int, c_int, c_int, c_int, UINT]
    SetWindowPos.restype = c_int
    SetWindowPos.errcheck = errcheck

    SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)

def errcheck(result, func, args):
    if not result:
        raise WinError(get_last_error())

if __name__ == "__main__":
    import pygame
    pygame.init()

    # win = pygame.display.set_mode((600, 400))
    win = pygame.display.set_mode((600, 400), pygame.RESIZABLE)

    hwnd = pygame.display.get_wm_info()["window"]
    set_window_topmost(hwnd)

    # regular pygame loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
