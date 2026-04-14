import ctypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002
VK_MENU = 0x12
VK_SHIFT = 0x10
VK_O = 0x4F
ULONG_PTR = ctypes.c_ulonglong if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_ulong

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ('wVk', ctypes.c_ushort),
        ('wScan', ctypes.c_ushort),
        ('dwFlags', ctypes.c_ulong),
        ('time', ctypes.c_ulong),
        ('dwExtraInfo', ULONG_PTR),
    ]

class _INPUTUNION(ctypes.Union):
    _fields_ = [('ki', KEYBDINPUT)]

class INPUT(ctypes.Structure):
    _anonymous_ = ('u',)
    _fields_ = [('type', ctypes.c_ulong), ('u', _INPUTUNION)]


def key_event(vk, flags=0):
    x = INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(wVk=vk, wScan=0, dwFlags=flags, time=0, dwExtraInfo=0))
    sent = user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(INPUT))
    if sent != 1:
        raise ctypes.WinError(ctypes.get_last_error())

# small delay so caller can switch focus if needed
time.sleep(0.3)
key_event(VK_MENU, 0)
key_event(VK_SHIFT, 0)
key_event(VK_O, 0)
time.sleep(0.05)
key_event(VK_O, KEYEVENTF_KEYUP)
key_event(VK_SHIFT, KEYEVENTF_KEYUP)
key_event(VK_MENU, KEYEVENTF_KEYUP)
print('sent Alt+Shift+O via SendInput')
