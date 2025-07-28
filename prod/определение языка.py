import ctypes

def get_layout():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4190419':
        l = 'ru'
    if hex(pf(0)) == '0x4090409':
        l = 'en'

get_layout()