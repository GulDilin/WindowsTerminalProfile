from ctypes import *
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
for color in range(16):
    windll.Kernel32.SetConsoleTextAttribute(h, color)
    print(f"color {color}")
