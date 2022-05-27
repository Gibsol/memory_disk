import os
import psutil
import platform

BYTE_TO_MEGABTE = 0.00000095367432
#memory
memory = psutil.virtual_memory()
memory_total = getattr(memory, 'total') * BYTE_TO_MEGABTE
memory_free = getattr(memory, 'free') * BYTE_TO_MEGABTE

#disk
disk = psutil.disk_usage('/')
disk_free = getattr(disk, 'total') * BYTE_TO_MEGABTE
disk_total = getattr(disk, 'free') * BYTE_TO_MEGABTE

# this block of code is required because Microsoft's cmd doesn't use "clear"
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print('RAM:')
print('your total memory: ', round(memory_total, 2), 'MB')
print('memory available: ', round(memory_free, 2), 'MB')

print('\nDisk usage:')
print('your total disk memory: ', round(disk_free, 2), 'MB')
print('disk memory available: ', round(disk_total, 2), 'MB')
